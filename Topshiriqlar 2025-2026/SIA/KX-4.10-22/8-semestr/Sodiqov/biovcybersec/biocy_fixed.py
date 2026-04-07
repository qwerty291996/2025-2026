from __future__ import annotations

import csv
import math
import os
import sys
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple

from PyQt5.QtCore import Qt, QRectF
from PyQt5.QtGui import QColor, QFont, QPainter, QPen
from PyQt5.QtWidgets import (
    QApplication,
    QComboBox,
    QFileDialog,
    QFormLayout,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QHeaderView,
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QSizePolicy,
    QTableWidget,
    QTableWidgetItem,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


# =========================
# Models
# =========================

@dataclass
class BrainSignalSample:
    sample_index: int = 0
    timestamp: datetime = field(default_factory=datetime.now)
    channels: Dict[str, float] = field(default_factory=dict)
    label: str = "normal"


@dataclass
class AttackDetectionResult:
    is_attack: bool = False
    attack_type: str = "None"
    confidence: float = 0.0
    risk_score: float = 0.0
    severity: str = "Past"
    description: str = "Hujum aniqlanmadi."
    channel_name: str = ""
    indicators: Dict[str, float] = field(default_factory=dict)


@dataclass
class IntentPrediction:
    expected_intent: str = ""
    predicted_intent: str = ""
    decoded_command: str = ""
    expected_action: str = ""
    canonical_expected: str = ""
    canonical_predicted: str = ""
    canonical_decoded: str = ""
    is_match: bool = False
    is_suspicious: bool = False
    confidence: float = 0.0
    mismatch_score: float = 0.0
    hijack_probability: float = 0.0
    recommended_action: str = "Allow"
    description: str = "Intent verification hali bajarilmagan."


@dataclass
class ProtectionAction:
    action_type: str = "Allow"
    block_command: bool = False
    safe_mode_enabled: bool = False
    show_alert: bool = False
    require_recheck: bool = False
    updated_risk_score: float = 0.0
    alert_message: str = "Tizim normal ishlamoqda."
    reason: str = "Himoya chorasi talab qilinmadi."


@dataclass
class SecurityEventLog:
    timestamp: datetime = field(default_factory=datetime.now)
    event_type: str = "Info"
    severity: str = "Past"
    source: str = "System"
    action_taken: str = "Allow"
    description: str = ""
    risk_score: float = 0.0


@dataclass
class UserBaselineProfile:
    total_samples: int = 0
    channel_count: int = 0
    channel_means: Dict[str, float] = field(default_factory=dict)
    channel_std_devs: Dict[str, float] = field(default_factory=dict)
    channel_variances: Dict[str, float] = field(default_factory=dict)
    channel_minimums: Dict[str, float] = field(default_factory=dict)
    channel_maximums: Dict[str, float] = field(default_factory=dict)
    channel_energies: Dict[str, float] = field(default_factory=dict)
    label_distribution: Dict[str, int] = field(default_factory=dict)


# =========================
# Services
# =========================

class RiskScoringService:
    def calculate_risk_score(self, attack_type: str, confidence: float, indicators: Dict[str, float]) -> float:
        attack_weight = self._get_attack_weight(attack_type)
        indicator_strength = self._get_indicator_strength(indicators)
        score = (attack_weight * 0.45) + (confidence * 0.40) + (indicator_strength * 0.15)
        return self._clamp(score, 0.0, 1.0)

    def get_severity(self, risk_score: float) -> str:
        if risk_score >= 0.85:
            return "Kritik"
        if risk_score >= 0.65:
            return "Yuqori"
        if risk_score >= 0.40:
            return "O‘rta"
        if risk_score >= 0.20:
            return "Past"
        return "Juda past"

    def _get_attack_weight(self, attack_type: str) -> float:
        mapping = {
            "Noise Injection": 0.55,
            "Replay Attack": 0.80,
            "Spoofing": 0.90,
            "Signal Tampering": 0.85,
            "Hijacked Command": 0.95,
            "None": 0.10,
        }
        return mapping.get(attack_type, 0.10)

    def _get_indicator_strength(self, indicators: Dict[str, float]) -> float:
        if not indicators:
            return 0.0
        values = [self._clamp(v, 0.0, 1.0) for v in indicators.values()]
        return sum(values) / len(values) if values else 0.0

    @staticmethod
    def _clamp(value: float, minimum: float, maximum: float) -> float:
        return max(minimum, min(maximum, value))


class DatasetReaderService:
    def load_from_csv(self, file_path: str, sampling_rate_hz: float) -> List[BrainSignalSample]:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Dataset topilmadi: {file_path}")

        with open(file_path, "r", encoding="utf-8-sig", newline="") as f:
            reader = csv.reader(f)
            rows = list(reader)

        if len(rows) < 2:
            raise ValueError("CSV ichida yetarli ma'lumot yo‘q.")

        headers = [h.strip() for h in rows[0]]
        valid_indexes = [
            i for i, h in enumerate(headers)
            if h and not h.lower().startswith("unnamed")
        ]
        if not valid_indexes:
            raise ValueError("Yaroqli EEG ustunlar topilmadi.")

        base_time = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        milliseconds_per_sample = 1000.0 / sampling_rate_hz

        samples: List[BrainSignalSample] = []
        for line_index, row in enumerate(rows[1:], start=1):
            if not row or all(not cell.strip() for cell in row):
                continue
            sample = BrainSignalSample(
                sample_index=line_index - 1,
                timestamp=base_time + timedelta(milliseconds=(line_index - 1) * milliseconds_per_sample),
                label="normal",
            )
            valid_row = True
            for column_index in valid_indexes:
                if column_index >= len(row):
                    valid_row = False
                    break
                raw_value = row[column_index].strip()
                try:
                    value = float(raw_value)
                except ValueError:
                    valid_row = False
                    break
                sample.channels[headers[column_index]] = value
            if valid_row and sample.channels:
                samples.append(sample)

        if not samples:
            raise ValueError("CSV dan birorta ham yaroqli sample o‘qilmadi.")
        return samples


class SignalPreprocessingService:
    def remove_invalid_samples(self, samples: List[BrainSignalSample]) -> List[BrainSignalSample]:
        return [s for s in samples if s and s.channels]

    def clamp_outliers(self, samples: List[BrainSignalSample], z_threshold: float) -> List[BrainSignalSample]:
        if not samples:
            return []
        source = self._clone_samples(samples)
        result = self._clone_samples(samples)
        channel_names = list(source[0].channels.keys())

        for channel in channel_names:
            values = [s.channels[channel] for s in source if channel in s.channels]
            if not values:
                continue
            mean = sum(values) / len(values)
            std = self._calculate_std(values, mean)
            if std == 0:
                continue
            min_allowed = mean - z_threshold * std
            max_allowed = mean + z_threshold * std
            for sample in result:
                if sample.channels[channel] < min_allowed:
                    sample.channels[channel] = min_allowed
                elif sample.channels[channel] > max_allowed:
                    sample.channels[channel] = max_allowed
        return result

    def apply_moving_average_smoothing(self, samples: List[BrainSignalSample], window_size: int) -> List[BrainSignalSample]:
        if not samples:
            return []
        if window_size < 1:
            window_size = 1
        source = self._clone_samples(samples)
        result = self._clone_samples(samples)
        channel_names = list(source[0].channels.keys())

        for i in range(len(source)):
            start = max(0, i - window_size + 1)
            window = source[start:i + 1]
            for channel in channel_names:
                avg = sum(s.channels[channel] for s in window) / len(window)
                result[i].channels[channel] = avg
        return result

    def normalize_min_max(self, samples: List[BrainSignalSample]) -> List[BrainSignalSample]:
        if not samples:
            return []
        result = self._clone_samples(samples)
        channel_names = list(result[0].channels.keys())
        for channel in channel_names:
            values = [s.channels[channel] for s in result]
            min_value, max_value = min(values), max(values)
            for sample in result:
                if abs(max_value - min_value) < 1e-6:
                    sample.channels[channel] = 0.0
                else:
                    sample.channels[channel] = (sample.channels[channel] - min_value) / (max_value - min_value)
        return result

    def run_full_pipeline(self, samples: List[BrainSignalSample]) -> List[BrainSignalSample]:
        cleaned = self.remove_invalid_samples(samples)
        clamped = self.clamp_outliers(cleaned, 3.0)
        smoothed = self.apply_moving_average_smoothing(clamped, 5)
        normalized = self.normalize_min_max(smoothed)
        return normalized

    @staticmethod
    def _calculate_std(values: List[float], mean: float) -> float:
        if not values:
            return 0.0
        variance = sum((v - mean) ** 2 for v in values) / len(values)
        return math.sqrt(variance)

    @staticmethod
    def _clone_samples(samples: List[BrainSignalSample]) -> List[BrainSignalSample]:
        clones: List[BrainSignalSample] = []
        for s in samples:
            clones.append(
                BrainSignalSample(
                    sample_index=s.sample_index,
                    timestamp=s.timestamp,
                    label=s.label,
                    channels=dict(s.channels),
                )
            )
        return clones


class PatternLearningService:
    def build_baseline_profile(self, samples: List[BrainSignalSample]) -> UserBaselineProfile:
        if not samples:
            raise ValueError("Baseline yaratish uchun sample yo‘q.")
        first_sample = samples[0]
        if not first_sample.channels:
            raise ValueError("Channel ma'lumotlari topilmadi.")

        channel_names = list(first_sample.channels.keys())
        profile = UserBaselineProfile(total_samples=len(samples), channel_count=len(channel_names))

        for channel in channel_names:
            values = [s.channels[channel] for s in samples if channel in s.channels]
            if not values:
                continue
            mean = sum(values) / len(values)
            variance = sum((v - mean) ** 2 for v in values) / len(values)
            std = math.sqrt(variance)
            min_value = min(values)
            max_value = max(values)
            energy = sum(v * v for v in values) / len(values)
            profile.channel_means[channel] = mean
            profile.channel_variances[channel] = variance
            profile.channel_std_devs[channel] = std
            profile.channel_minimums[channel] = min_value
            profile.channel_maximums[channel] = max_value
            profile.channel_energies[channel] = energy

        for s in samples:
            if s.label:
                profile.label_distribution[s.label] = profile.label_distribution.get(s.label, 0) + 1
        return profile


class AttackDetectionService:
    def __init__(self) -> None:
        self.risk_scoring_service = RiskScoringService()

    def analyze_channel(
        self,
        samples: List[BrainSignalSample],
        baseline_profile: UserBaselineProfile,
        channel_name: str,
    ) -> AttackDetectionResult:
        if not samples:
            raise ValueError("Analiz uchun sample topilmadi.")
        if baseline_profile is None:
            raise ValueError("Normal profil topilmadi. Avval baseline yarating.")
        if not channel_name.strip():
            raise ValueError("Kanal nomi tanlanmagan.")

        values = [s.channels[channel_name] for s in samples if channel_name in s.channels]
        if not values:
            raise ValueError("Tanlangan kanal uchun qiymatlar topilmadi.")

        candidates: List[AttackDetectionResult] = []
        for detector in (
            self._detect_noise_injection,
            self._detect_replay_attack,
            self._detect_spoofing,
            self._detect_signal_tampering,
        ):
            result = detector(values, baseline_profile, channel_name)
            if result.confidence > 0.20:
                candidates.append(result)

        if not candidates:
            return AttackDetectionResult(
                is_attack=False,
                attack_type="None",
                confidence=0.05,
                risk_score=0.05,
                severity="Juda past",
                description="Tanlangan kanal bo‘yicha aniq hujum belgisi topilmadi.",
                channel_name=channel_name,
            )

        candidates.sort(key=lambda c: (c.risk_score, c.confidence), reverse=True)
        return candidates[0]

    def _detect_noise_injection(
        self, values: List[float], baseline_profile: UserBaselineProfile, channel_name: str
    ) -> AttackDetectionResult:
        result = AttackDetectionResult(attack_type="Noise Injection", channel_name=channel_name)
        if channel_name not in baseline_profile.channel_variances or channel_name not in baseline_profile.channel_std_devs:
            return result

        current_variance = self._calculate_variance(values)
        baseline_variance = baseline_profile.channel_variances[channel_name]
        baseline_std = baseline_profile.channel_std_devs[channel_name]

        variance_ratio = current_variance / baseline_variance if baseline_variance > 1e-6 else 0.0
        avg_delta = self._calculate_average_delta(values)
        delta_score = avg_delta / (baseline_std * 1.5) if baseline_std > 1e-6 else 0.0

        confidence = (
            self._normalize_ratio(variance_ratio, 1.2, 4.0) * 0.65
            + self._normalize_ratio(delta_score, 0.8, 3.0) * 0.35
        )
        confidence = self._clamp(confidence, 0.0, 1.0)

        result.confidence = confidence
        result.is_attack = confidence >= 0.45
        result.indicators["VarianceRatio"] = self._clamp(variance_ratio / 4.0, 0.0, 1.0)
        result.indicators["DeltaScore"] = self._clamp(delta_score / 3.0, 0.0, 1.0)
        result.risk_score = self.risk_scoring_service.calculate_risk_score(result.attack_type, result.confidence, result.indicators)
        result.severity = self.risk_scoring_service.get_severity(result.risk_score)
        result.description = "Signal variansi baseline’dan keskin oshgan yoki ketma-ket nuqtalar orasidagi farq juda yuqori."
        return result

    def _detect_replay_attack(
        self, values: List[float], _: UserBaselineProfile, channel_name: str
    ) -> AttackDetectionResult:
        result = AttackDetectionResult(attack_type="Replay Attack", channel_name=channel_name)
        if len(values) < 64:
            return result

        window_size = 16
        step = 8
        signatures: Dict[str, int] = {}
        repeated_windows = 0
        total_windows = 0

        for i in range(0, len(values) - window_size + 1, step):
            window = values[i:i + window_size]
            signature = self._build_window_signature(window)
            if signature in signatures:
                signatures[signature] += 1
                repeated_windows += 1
            else:
                signatures[signature] = 1
            total_windows += 1

        repeat_ratio = repeated_windows / total_windows if total_windows else 0.0
        confidence = self._clamp(self._normalize_ratio(repeat_ratio, 0.08, 0.45), 0.0, 1.0)

        result.confidence = confidence
        result.is_attack = confidence >= 0.50
        result.indicators["RepeatRatio"] = self._clamp(repeat_ratio / 0.45, 0.0, 1.0)
        result.risk_score = self.risk_scoring_service.calculate_risk_score(result.attack_type, result.confidence, result.indicators)
        result.severity = self.risk_scoring_service.get_severity(result.risk_score)
        result.description = "Signal oynalari orasida g‘ayritabiiy takrorlanish bor. Bu replay hujumiga o‘xshashi mumkin."
        return result

    def _detect_spoofing(
        self, values: List[float], baseline_profile: UserBaselineProfile, channel_name: str
    ) -> AttackDetectionResult:
        result = AttackDetectionResult(attack_type="Spoofing", channel_name=channel_name)
        if (
            channel_name not in baseline_profile.channel_means
            or channel_name not in baseline_profile.channel_std_devs
            or channel_name not in baseline_profile.channel_energies
        ):
            return result

        baseline_mean = baseline_profile.channel_means[channel_name]
        baseline_std = baseline_profile.channel_std_devs[channel_name]
        baseline_energy = baseline_profile.channel_energies[channel_name]
        current_mean = sum(values) / len(values)
        current_energy = self._calculate_energy(values)

        expected_min = baseline_mean - (3.0 * baseline_std)
        expected_max = baseline_mean + (3.0 * baseline_std)
        out_of_range_count = len([v for v in values if v < expected_min or v > expected_max])
        out_of_range_ratio = out_of_range_count / len(values)
        mean_shift = abs(current_mean - baseline_mean) / baseline_std if baseline_std > 1e-6 else 0.0
        energy_ratio = current_energy / baseline_energy if baseline_energy > 1e-6 else 0.0

        confidence = (
            self._clamp(out_of_range_ratio * 2.0, 0.0, 1.0) * 0.50
            + self._normalize_ratio(mean_shift, 0.8, 4.0) * 0.30
            + self._normalize_ratio(abs(energy_ratio - 1.0), 0.15, 1.5) * 0.20
        )
        confidence = self._clamp(confidence, 0.0, 1.0)

        result.confidence = confidence
        result.is_attack = confidence >= 0.50
        result.indicators["OutOfRangeRatio"] = self._clamp(out_of_range_ratio * 2.0, 0.0, 1.0)
        result.indicators["MeanShift"] = self._clamp(mean_shift / 4.0, 0.0, 1.0)
        result.indicators["EnergyDifference"] = self._clamp(abs(energy_ratio - 1.0) / 1.5, 0.0, 1.0)
        result.risk_score = self.risk_scoring_service.calculate_risk_score(result.attack_type, result.confidence, result.indicators)
        result.severity = self.risk_scoring_service.get_severity(result.risk_score)
        result.description = "Signal foydalanuvchining baseline profili bilan yetarli mos emas."
        return result

    def _detect_signal_tampering(
        self, values: List[float], baseline_profile: UserBaselineProfile, channel_name: str
    ) -> AttackDetectionResult:
        result = AttackDetectionResult(attack_type="Signal Tampering", channel_name=channel_name)
        if channel_name not in baseline_profile.channel_minimums or channel_name not in baseline_profile.channel_maximums:
            return result

        current_min = min(values)
        current_max = max(values)
        current_range = current_max - current_min
        baseline_min = baseline_profile.channel_minimums[channel_name]
        baseline_max = baseline_profile.channel_maximums[channel_name]
        baseline_range = baseline_max - baseline_min

        zero_count = len([v for v in values if abs(v) < 1e-6])
        zero_ratio = zero_count / len(values)
        flat_count = sum(1 for i in range(1, len(values)) if abs(values[i] - values[i - 1]) < 1e-6)
        flat_ratio = flat_count / (len(values) - 1) if len(values) > 1 else 0.0
        scale_difference = abs(current_range - baseline_range) / baseline_range if baseline_range > 1e-6 else 0.0

        confidence = (
            self._clamp(zero_ratio * 2.5, 0.0, 1.0) * 0.35
            + self._clamp(flat_ratio * 2.0, 0.0, 1.0) * 0.30
            + self._normalize_ratio(scale_difference, 0.20, 2.0) * 0.35
        )
        confidence = self._clamp(confidence, 0.0, 1.0)

        result.confidence = confidence
        result.is_attack = confidence >= 0.45
        result.indicators["ZeroRatio"] = self._clamp(zero_ratio * 2.5, 0.0, 1.0)
        result.indicators["FlatRatio"] = self._clamp(flat_ratio * 2.0, 0.0, 1.0)
        result.indicators["ScaleDifference"] = self._clamp(scale_difference / 2.0, 0.0, 1.0)
        result.risk_score = self.risk_scoring_service.calculate_risk_score(result.attack_type, result.confidence, result.indicators)
        result.severity = self.risk_scoring_service.get_severity(result.risk_score)
        result.description = "Signalda nol segmentlar, tekis chiziq yoki amplitude masshtabi o‘zgarishi aniqlandi."
        return result

    @staticmethod
    def _calculate_variance(values: List[float]) -> float:
        if not values:
            return 0.0
        mean = sum(values) / len(values)
        return sum((v - mean) ** 2 for v in values) / len(values)

    @staticmethod
    def _calculate_average_delta(values: List[float]) -> float:
        if len(values) < 2:
            return 0.0
        return sum(abs(values[i] - values[i - 1]) for i in range(1, len(values))) / (len(values) - 1)

    @staticmethod
    def _calculate_energy(values: List[float]) -> float:
        if not values:
            return 0.0
        return sum(v * v for v in values) / len(values)

    def _build_window_signature(self, window: List[float]) -> str:
        if not window:
            return ""
        min_value, max_value = min(window), max(window)
        if abs(max_value - min_value) < 1e-6:
            return "FLAT"
        buckets = []
        for value in window:
            normalized = (value - min_value) / (max_value - min_value)
            bucket = int(round(normalized * 9.0))
            buckets.append(bucket)
        return "-".join(map(str, buckets))

    @staticmethod
    def _normalize_ratio(value: float, start: float, end: float) -> float:
        if value <= start:
            return 0.0
        if value >= end:
            return 1.0
        return (value - start) / (end - start)

    @staticmethod
    def _clamp(value: float, minimum: float, maximum: float) -> float:
        return max(minimum, min(maximum, value))


class IntentVerificationService:
    def verify_intent(
        self,
        predicted_intent: str,
        decoded_command: str,
        expected_action: str,
        confidence: float,
    ) -> IntentPrediction:
        result = IntentPrediction()
        result.predicted_intent = predicted_intent or ""
        result.decoded_command = decoded_command or ""
        result.expected_action = expected_action or ""
        result.confidence = self._clamp(confidence, 0.0, 1.0)
        source_expected = expected_action if expected_action.strip() else predicted_intent
        result.expected_intent = source_expected or ""
        result.canonical_expected = self._normalize_command(source_expected)
        result.canonical_predicted = self._normalize_command(predicted_intent)
        result.canonical_decoded = self._normalize_command(decoded_command)

        mismatch_score = self._calculate_mismatch_score(
            result.canonical_expected,
            result.canonical_predicted,
            result.canonical_decoded,
        )
        hijack_probability = self._calculate_hijack_probability(
            result.canonical_expected,
            result.canonical_predicted,
            result.canonical_decoded,
            result.confidence,
            mismatch_score,
        )

        result.mismatch_score = mismatch_score
        result.hijack_probability = hijack_probability
        result.is_match = result.canonical_expected == result.canonical_decoded
        result.is_suspicious = hijack_probability >= 0.45
        result.recommended_action = self._get_recommended_action(hijack_probability)
        result.description = self._build_description(result)
        return result

    def _calculate_mismatch_score(self, expected: str, predicted: str, decoded: str) -> float:
        expected_decoded = self._get_pair_mismatch_severity(expected, decoded)
        predicted_decoded = self._get_pair_mismatch_severity(predicted, decoded)
        expected_predicted = self._get_pair_mismatch_severity(expected, predicted)
        score = (expected_decoded * 0.55) + (predicted_decoded * 0.30) + (expected_predicted * 0.15)
        return self._clamp(score, 0.0, 1.0)

    def _calculate_hijack_probability(
        self,
        expected: str,
        predicted: str,
        decoded: str,
        confidence: float,
        mismatch_score: float,
    ) -> float:
        confidence_boost = confidence * 0.20
        expected_decoded_boost = 0.15 if expected != decoded else 0.0
        full_conflict = (
            expected != decoded
            and predicted != decoded
            and predicted != expected
            and expected != "UNKNOWN"
            and predicted != "UNKNOWN"
            and decoded != "UNKNOWN"
        )
        triad_conflict_boost = 0.15 if full_conflict else 0.0
        probability = mismatch_score + confidence_boost + expected_decoded_boost + triad_conflict_boost
        return self._clamp(probability, 0.0, 1.0)

    @staticmethod
    def _get_recommended_action(hijack_probability: float) -> str:
        if hijack_probability >= 0.80:
            return "Block"
        if hijack_probability >= 0.60:
            return "RequireRecheck"
        if hijack_probability >= 0.45:
            return "Warn"
        return "Allow"

    def _build_description(self, result: IntentPrediction) -> str:
        if not result.is_suspicious and result.is_match:
            return "Decoded command foydalanuvchi kutilgan niyati bilan mos. Shubhali holat aniqlanmadi."
        if result.recommended_action == "Block":
            return "Intent mismatch yuqori darajada. Neural command hijacking yoki decoder buzilishi ehtimoli katta. Buyruqni bloklash tavsiya etiladi."
        if result.recommended_action == "RequireRecheck":
            return "Intent va decoded command orasida sezilarli nomoslik bor. Qayta tekshiruv yoki qayta decoding talab etiladi."
        if result.recommended_action == "Warn":
            return "Qisman nomoslik bor. Bu oddiy xato, signal buzilishi yoki boshlang‘ich hijack alomati bo‘lishi mumkin."
        return "Intent verification bajarildi. Holat hozircha kritik emas."

    def _get_pair_mismatch_severity(self, a: str, b: str) -> float:
        if a == b:
            return 0.0
        if a == "UNKNOWN" or b == "UNKNOWN":
            return 0.55
        if self._is_opposite(a, b):
            return 1.0
        if ((a == "STOP" and self._is_movement(b)) or (b == "STOP" and self._is_movement(a))):
            return 0.95
        if ((a == "REST" and self._is_movement(b)) or (b == "REST" and self._is_movement(a))):
            return 0.85
        if self._is_movement(a) and self._is_movement(b):
            return 0.70
        return 0.60

    @staticmethod
    def _is_opposite(a: str, b: str) -> bool:
        return (
            (a == "MOVE_LEFT" and b == "MOVE_RIGHT")
            or (a == "MOVE_RIGHT" and b == "MOVE_LEFT")
            or (a == "MOVE_FORWARD" and b == "MOVE_BACKWARD")
            or (a == "MOVE_BACKWARD" and b == "MOVE_FORWARD")
        )

    @staticmethod
    def _is_movement(value: str) -> bool:
        return value in {"MOVE_LEFT", "MOVE_RIGHT", "MOVE_FORWARD", "MOVE_BACKWARD"}

    @staticmethod
    def _normalize_command(value: str) -> str:
        if not value or not value.strip():
            return "UNKNOWN"
        text = value.strip().lower()
        mappings = {
            "left": "MOVE_LEFT",
            "move_left": "MOVE_LEFT",
            "chap": "MOVE_LEFT",
            "chapga": "MOVE_LEFT",
            "chapga yur": "MOVE_LEFT",
            "chapga yurish": "MOVE_LEFT",
            "right": "MOVE_RIGHT",
            "move_right": "MOVE_RIGHT",
            "o'ng": "MOVE_RIGHT",
            "ong": "MOVE_RIGHT",
            "o‘ng": "MOVE_RIGHT",
            "o‘ngga": "MOVE_RIGHT",
            "ongga": "MOVE_RIGHT",
            "o‘ngga yur": "MOVE_RIGHT",
            "o‘ngga yurish": "MOVE_RIGHT",
            "forward": "MOVE_FORWARD",
            "move_forward": "MOVE_FORWARD",
            "oldinga": "MOVE_FORWARD",
            "oldinga yur": "MOVE_FORWARD",
            "oldinga yurish": "MOVE_FORWARD",
            "backward": "MOVE_BACKWARD",
            "move_backward": "MOVE_BACKWARD",
            "orqaga": "MOVE_BACKWARD",
            "orqaga yur": "MOVE_BACKWARD",
            "orqaga yurish": "MOVE_BACKWARD",
            "stop": "STOP",
            "toxta": "STOP",
            "to'xta": "STOP",
            "to‘xta": "STOP",
            "stop command": "STOP",
            "rest": "REST",
            "tinch": "REST",
            "kutish": "REST",
            "select": "SELECT",
            "tanla": "SELECT",
        }
        return mappings.get(text, text.upper())

    @staticmethod
    def _clamp(value: float, minimum: float, maximum: float) -> float:
        return max(minimum, min(maximum, value))


class ProtectionService:
    def decide_protection(
        self,
        attack_result: Optional[AttackDetectionResult],
        intent_prediction: Optional[IntentPrediction],
    ) -> ProtectionAction:
        action = ProtectionAction()
        attack_risk = attack_result.risk_score if attack_result else 0.0
        hijack_risk = intent_prediction.hijack_probability if intent_prediction else 0.0
        final_risk = max(attack_risk, hijack_risk)
        action.updated_risk_score = final_risk

        has_attack = bool(attack_result and attack_result.is_attack)
        suspicious_intent = bool(intent_prediction and intent_prediction.is_suspicious)

        if final_risk >= 0.80:
            action.action_type = "SafeMode"
            action.block_command = True
            action.safe_mode_enabled = True
            action.show_alert = True
            action.require_recheck = True
            action.alert_message = "Kritik xavf aniqlandi. Tizim Safe Mode holatiga o‘tkazildi."
            action.reason = "RiskScore juda yuqori yoki command hijack ehtimoli kritik darajada."
            return action

        if suspicious_intent and final_risk >= 0.60:
            action.action_type = "Block"
            action.block_command = True
            action.safe_mode_enabled = False
            action.show_alert = True
            action.require_recheck = True
            action.alert_message = "Intent mismatch aniqlandi. Buyruq bloklandi."
            action.reason = "Decoded command foydalanuvchi niyatiga mos emas."
            return action

        if has_attack and final_risk >= 0.50:
            action.action_type = "RequireRecheck"
            action.block_command = False
            action.safe_mode_enabled = False
            action.show_alert = True
            action.require_recheck = True
            action.alert_message = "Shubhali signal topildi. Qayta tekshirish talab qilinadi."
            action.reason = "Signalda tahdid alomatlari bor, lekin kritik emas."
            return action

        if has_attack or suspicious_intent:
            action.action_type = "Warn"
            action.block_command = False
            action.safe_mode_enabled = False
            action.show_alert = True
            action.require_recheck = False
            action.alert_message = "Ogohlantirish: tizimda shubhali holat topildi."
            action.reason = "Risk past yoki o‘rta darajada, monitoring davom etadi."
            return action

        return action


class LoggingService:
    def __init__(self) -> None:
        self._logs: List[SecurityEventLog] = []

    def add_log(self, log: SecurityEventLog) -> None:
        if log:
            self._logs.append(log)

    def get_all_logs(self) -> List[SecurityEventLog]:
        return list(self._logs)

    def clear_logs(self) -> None:
        self._logs.clear()

    def export_to_csv(self, file_path: str) -> None:
        with open(file_path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["TimeStamp", "EventType", "Severity", "Source", "ActionTaken", "RiskScore", "Description"])
            for log in self._logs:
                writer.writerow([
                    log.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                    log.event_type,
                    log.severity,
                    log.source,
                    log.action_taken,
                    f"{log.risk_score:.3f}",
                    log.description,
                ])


# =========================
# Chart widget
# =========================

class SignalChartWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.values: List[float] = []
        self.channel_name: str = ""
        self.setMinimumHeight(280)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

    def set_signal(self, values: List[float], channel_name: str) -> None:
        self.values = values[:]
        self.channel_name = channel_name
        self.update()

    def clear_signal(self) -> None:
        self.values = []
        self.channel_name = ""
        self.update()

    def paintEvent(self, event) -> None:  # type: ignore[override]
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        rect = self.rect().adjusted(10, 10, -10, -10)

        painter.fillRect(self.rect(), QColor("#0B1220"))
        painter.setPen(QPen(QColor("#1F314F"), 1))
        painter.drawRoundedRect(rect, 14, 14)

        if not self.values:
            painter.setPen(QColor("#8FA4C7"))
            painter.drawText(rect, Qt.AlignCenter, "Grafik ko‘rsatish uchun signal yuklang")
            return

        min_val = min(self.values)
        max_val = max(self.values)
        if abs(max_val - min_val) < 1e-9:
            max_val = min_val + 1.0

        inner = rect.adjusted(20, 20, -20, -28)

        grid_pen = QPen(QColor("#15263E"), 1)
        painter.setPen(grid_pen)
        for i in range(5):
            y = inner.top() + i * inner.height() / 4.0
            painter.drawLine(int(inner.left()), int(y), int(inner.right()), int(y))

        line_pen = QPen(QColor("#22D3EE"), 2)
        painter.setPen(line_pen)
        n = len(self.values)
        points = []
        for idx, value in enumerate(self.values):
            x = inner.left() + (idx / max(1, n - 1)) * inner.width()
            normalized = (value - min_val) / (max_val - min_val)
            y = inner.bottom() - normalized * inner.height()
            points.append((x, y))

        for i in range(1, len(points)):
            painter.drawLine(int(points[i - 1][0]), int(points[i - 1][1]), int(points[i][0]), int(points[i][1]))

        painter.setPen(QColor("#A9BDD9"))
        painter.setFont(QFont("Segoe UI", 9))
        painter.drawText(QRectF(inner.left(), rect.bottom() - 20, inner.width(), 18), Qt.AlignLeft, f"Kanal: {self.channel_name}")
        painter.drawText(QRectF(inner.left(), inner.top() - 18, inner.width(), 18), Qt.AlignRight, f"Min: {min_val:.3f}   Max: {max_val:.3f}")


# =========================
# Main Window
# =========================

class CardFrame(QFrame):
    def __init__(self) -> None:
        super().__init__()
        self.setObjectName("card")


class NeuroShieldWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("NeuroShield - PyQt5 Cyber Defense Dashboard")
        self.resize(1600, 980)

        self.dataset_reader_service = DatasetReaderService()
        self.signal_preprocessing_service = SignalPreprocessingService()
        self.pattern_learning_service = PatternLearningService()
        self.attack_detection_service = AttackDetectionService()
        self.intent_verification_service = IntentVerificationService()
        self.protection_service = ProtectionService()
        self.logging_service = LoggingService()

        self.raw_samples: List[BrainSignalSample] = []
        self.processed_samples: List[BrainSignalSample] = []
        self.baseline_profile: Optional[UserBaselineProfile] = None
        self.attack_detection_result: Optional[AttackDetectionResult] = None
        self.intent_prediction: Optional[IntentPrediction] = None
        self.protection_action: Optional[ProtectionAction] = None
        self.current_file_path: str = ""

        self._setup_ui()
        self._apply_styles()
        self._reset_views()

    def _setup_ui(self) -> None:
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(18, 18, 18, 18)
        main_layout.setSpacing(12)

        header = self._build_header()
        controls = self._build_controls()
        content = self._build_main_content()
        logs = self._build_logs_section()

        main_layout.addWidget(header)
        main_layout.addWidget(controls)
        main_layout.addLayout(content, 1)
        main_layout.addWidget(logs, 1)

    def _build_header(self) -> QWidget:
        card = CardFrame()
        layout = QHBoxLayout(card)
        layout.setContentsMargins(20, 20, 20, 20)

        left = QVBoxLayout()
        title = QLabel("NeuroShield")
        title.setObjectName("title")
        subtitle = QLabel(
            "BCI kiberhimoya paneli — dataset, preprocessing, baseline, hujumni aniqlash, intent verification va protection engine"
        )
        subtitle.setWordWrap(True)
        subtitle.setObjectName("subtitle")
        left.addWidget(title)
        left.addWidget(subtitle)

        right = CardFrame()
        right.setObjectName("statusCard")
        right_layout = QVBoxLayout(right)
        right_layout.setContentsMargins(16, 14, 16, 14)
        label = QLabel("Tizim holati")
        label.setObjectName("muted")
        self.lbl_status = QLabel("Tayyor emas")
        self.lbl_status.setObjectName("statusWarning")
        right_layout.addWidget(label)
        right_layout.addWidget(self.lbl_status)

        layout.addLayout(left, 1)
        layout.addWidget(right)
        return card

    def _build_controls(self) -> QWidget:
        card = CardFrame()
        layout = QVBoxLayout(card)
        layout.setContentsMargins(18, 18, 18, 18)
        layout.setSpacing(12)

        button_row = QHBoxLayout()
        button_row.setSpacing(10)

        self.btn_load = self._make_button("EEG faylni yuklash", self.load_dataset, "#2563EB")
        self.btn_pipeline = self._make_button("Qayta ishlash", self.run_pipeline, "#0891B2")
        self.btn_baseline = self._make_button("Normal profil yaratish", self.build_baseline, "#059669")
        self.btn_attack = self._make_button("Hujumni aniqlash", self.detect_attack, "#7C3AED")
        self.btn_intent = self._make_button("Niyatni tekshirish", self.verify_intent, "#EA580C")
        self.btn_protect = self._make_button("Himoya chorasi", self.apply_protection, "#14B8A6")
        self.btn_export = self._make_button("Loglarni export", self.export_logs, "#475569")
        self.btn_reset = self._make_button("Tozalash", self.reset_all, "#DC2626")

        for btn in [
            self.btn_load,
            self.btn_pipeline,
            self.btn_baseline,
            self.btn_attack,
            self.btn_intent,
            self.btn_protect,
            self.btn_export,
            self.btn_reset,
        ]:
            button_row.addWidget(btn)
        button_row.addStretch(1)
        layout.addLayout(button_row)

        form_layout = QGridLayout()
        form_layout.setHorizontalSpacing(16)
        form_layout.setVerticalSpacing(10)

        self.cmb_channel = QComboBox()
        self.cmb_channel.currentTextChanged.connect(self.on_channel_changed)
        self.txt_sampling_rate = QLineEdit("128")
        self.lbl_loaded_file = QLabel("Hozircha fayl yuklanmagan")
        self.lbl_loaded_file.setWordWrap(True)
        self.lbl_loaded_file.setObjectName("body")

        self.txt_expected_action = QLineEdit("chapga yurish")
        self.txt_predicted_intent = QLineEdit("chapga yurish")
        self.txt_decoded_command = QLineEdit("o‘ngga yurish")
        self.txt_intent_confidence = QLineEdit("0.92")

        form_layout.addWidget(self._make_label("Kanal tanlash"), 0, 0)
        form_layout.addWidget(self._make_label("Sampling rate (Hz)"), 0, 1)
        form_layout.addWidget(self._make_label("Yuklangan fayl"), 0, 2)
        form_layout.addWidget(self.cmb_channel, 1, 0)
        form_layout.addWidget(self.txt_sampling_rate, 1, 1)
        form_layout.addWidget(self.lbl_loaded_file, 1, 2)

        form_layout.addWidget(self._make_label("Expected action"), 2, 0)
        form_layout.addWidget(self._make_label("Predicted intent"), 2, 1)
        form_layout.addWidget(self._make_label("Decoded command"), 2, 2)
        form_layout.addWidget(self.txt_expected_action, 3, 0)
        form_layout.addWidget(self.txt_predicted_intent, 3, 1)
        form_layout.addWidget(self.txt_decoded_command, 3, 2)
        form_layout.addWidget(self._make_label("Intent confidence (0-1)"), 2, 3)
        form_layout.addWidget(self.txt_intent_confidence, 3, 3)

        form_layout.setColumnStretch(2, 1)
        layout.addLayout(form_layout)
        return card

    def _build_main_content(self) -> QHBoxLayout:
        layout = QHBoxLayout()
        layout.setSpacing(14)

        left = QVBoxLayout()
        right = QVBoxLayout()

        chart_card = CardFrame()
        chart_layout = QVBoxLayout(chart_card)
        chart_layout.setContentsMargins(18, 18, 18, 18)
        chart_layout.addWidget(self._section_title("Signal grafigi"))
        self.lbl_chart_info = QLabel("Grafik ko‘rsatish uchun EEG fayl yuklang.")
        self.lbl_chart_info.setObjectName("body")
        self.chart_widget = SignalChartWidget()
        chart_layout.addWidget(self.lbl_chart_info)
        chart_layout.addWidget(self.chart_widget, 1)

        preview_card = CardFrame()
        preview_layout = QVBoxLayout(preview_card)
        preview_layout.setContentsMargins(18, 18, 18, 18)
        preview_layout.addWidget(self._section_title("Signal namunalari"))
        self.lst_preview = QListWidget()
        preview_layout.addWidget(self.lst_preview)

        left.addWidget(chart_card, 3)
        left.addWidget(preview_card, 2)

        attack_card = CardFrame()
        attack_layout = QVBoxLayout(attack_card)
        attack_layout.setContentsMargins(18, 18, 18, 18)
        attack_layout.addWidget(self._section_title("Attack Detection"))
        self.txt_attack_report = QTextEdit()
        self.txt_attack_report.setReadOnly(True)
        attack_layout.addWidget(self.txt_attack_report)

        intent_card = CardFrame()
        intent_layout = QVBoxLayout(intent_card)
        intent_layout.setContentsMargins(18, 18, 18, 18)
        intent_layout.addWidget(self._section_title("Intent Verification"))
        self.txt_intent_report = QTextEdit()
        self.txt_intent_report.setReadOnly(True)
        intent_layout.addWidget(self.txt_intent_report)

        protection_card = CardFrame()
        protection_layout = QVBoxLayout(protection_card)
        protection_layout.setContentsMargins(18, 18, 18, 18)
        protection_layout.addWidget(self._section_title("Protection Engine"))
        self.txt_protection_report = QTextEdit()
        self.txt_protection_report.setReadOnly(True)
        protection_layout.addWidget(self.txt_protection_report)

        dashboard_card = CardFrame()
        dashboard_layout = QGridLayout(dashboard_card)
        dashboard_layout.setContentsMargins(18, 18, 18, 18)
        dashboard_layout.addWidget(self._section_title("Dashboard"), 0, 0, 1, 2)
        self.card_total_samples, self.lbl_total_samples = self._stat_box("Total samples", "0")
        self.card_total_channels, self.lbl_total_channels = self._stat_box("Channel count", "0")
        self.card_selected_channel, self.lbl_selected_channel = self._stat_box("Tanlangan kanal", "-")
        self.card_risk, self.lbl_risk = self._stat_box("Updated risk", "0.00")
        dashboard_layout.addWidget(self.card_total_samples, 1, 0)
        dashboard_layout.addWidget(self.card_total_channels, 1, 1)
        dashboard_layout.addWidget(self.card_selected_channel, 2, 0)
        dashboard_layout.addWidget(self.card_risk, 2, 1)

        right.addWidget(dashboard_card, 1)
        right.addWidget(attack_card, 2)
        right.addWidget(intent_card, 2)
        right.addWidget(protection_card, 2)

        layout.addLayout(left, 3)
        layout.addLayout(right, 2)
        return layout

    def _build_logs_section(self) -> QWidget:
        card = CardFrame()
        layout = QVBoxLayout(card)
        layout.setContentsMargins(18, 18, 18, 18)
        layout.addWidget(self._section_title("Security logs"))

        self.tbl_logs = QTableWidget(0, 6)
        self.tbl_logs.setHorizontalHeaderLabels(["Vaqt", "Event", "Severity", "Source", "Action", "Risk"])
        self.tbl_logs.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tbl_logs.verticalHeader().setVisible(False)
        self.tbl_logs.setSelectionBehavior(QTableWidget.SelectRows)
        self.tbl_logs.setEditTriggers(QTableWidget.NoEditTriggers)
        layout.addWidget(self.tbl_logs)
        return card

    def _make_button(self, text: str, handler, color: str) -> QPushButton:
        button = QPushButton(text)
        button.clicked.connect(handler)
        button.setStyleSheet(
            f"QPushButton {{ background:{color}; border:none; border-radius:14px; padding:12px 16px; font-weight:600; color:white; }}"
            f"QPushButton:hover {{ background:{self._lighter(color)}; }}"
        )
        return button

    def _stat_box(self, title: str, value: str) -> Tuple[QWidget, QLabel]:
        frame = CardFrame()
        frame.setObjectName("statCard")
        layout = QVBoxLayout(frame)
        layout.setContentsMargins(14, 12, 14, 12)
        t = QLabel(title)
        t.setObjectName("muted")
        v = QLabel(value)
        v.setObjectName("statValue")
        layout.addWidget(t)
        layout.addWidget(v)
        return frame, v

    def _section_title(self, text: str) -> QLabel:
        label = QLabel(text)
        label.setObjectName("sectionTitle")
        return label

    def _make_label(self, text: str) -> QLabel:
        label = QLabel(text)
        label.setObjectName("muted")
        return label

    def _apply_styles(self) -> None:
        self.setStyleSheet(
            """
            QMainWindow, QWidget {
                background: #07101D;
                color: white;
                font-family: 'Segoe UI';
                font-size: 13px;
            }
            QFrame#card {
                background: #101A2C;
                border: 1px solid #1C2A44;
                border-radius: 22px;
            }
            QFrame#statusCard {
                background: #0E1A2D;
                border: 1px solid #233754;
                border-radius: 18px;
            }
            QFrame#statCard {
                background: #0A1220;
                border: 1px solid #1B2C48;
                border-radius: 18px;
            }
            QLabel#title {
                font-size: 30px;
                font-weight: 700;
            }
            QLabel#subtitle {
                color: #A9BDD9;
                font-size: 14px;
            }
            QLabel#sectionTitle {
                font-size: 18px;
                font-weight: 700;
                color: white;
            }
            QLabel#muted {
                color: #8FA4C7;
                font-size: 12px;
            }
            QLabel#body {
                color: #D7E3F4;
                font-size: 13px;
            }
            QLabel#statusWarning {
                color: #FACC15;
                font-size: 22px;
                font-weight: 700;
            }
            QLabel#statusGood {
                color: #22C55E;
                font-size: 22px;
                font-weight: 700;
            }
            QLabel#statusDanger {
                color: #FB7185;
                font-size: 22px;
                font-weight: 700;
            }
            QLabel#statValue {
                font-size: 24px;
                font-weight: 700;
                color: white;
            }
            QLineEdit, QComboBox, QTextEdit, QListWidget, QTableWidget {
                background: #0B1220;
                border: 1px solid #26364F;
                border-radius: 12px;
                padding: 8px;
                color: white;
                selection-background-color: #2563EB;
            }
            QHeaderView::section {
                background: #0E1A2D;
                color: #B8CAE6;
                border: none;
                padding: 8px;
                font-weight: 600;
            }
            QListWidget::item {
                padding: 6px;
            }
            """
        )

    # =========================
    # Actions
    # =========================

    def load_dataset(self) -> None:
        try:
            file_path, _ = QFileDialog.getOpenFileName(self, "EEG CSV faylni tanlang", "", "CSV Files (*.csv)")
            if not file_path:
                return
            sampling_rate = self._get_sampling_rate()
            self.raw_samples = self.dataset_reader_service.load_from_csv(file_path, sampling_rate)
            self.processed_samples = []
            self.baseline_profile = None
            self.attack_detection_result = None
            self.protection_action = None
            self.current_file_path = file_path
            self.lbl_loaded_file.setText(file_path)
            self._fill_channel_combo()
            self._update_dashboard()
            self._log("Dataset", "Info", "DatasetReader", "Load", f"{len(self.raw_samples)} sample yuklandi.", 0.05)
            self._set_status("Dataset yuklandi", "good")
            self._update_preview()
            self._draw_chart()
            self.txt_attack_report.setPlainText("Dataset yuklandi. Endi preprocessing va baseline yarating.")
        except Exception as ex:
            self._show_error(str(ex))

    def run_pipeline(self) -> None:
        try:
            if not self.raw_samples:
                raise ValueError("Avval EEG dataset yuklang.")
            self.processed_samples = self.signal_preprocessing_service.run_full_pipeline(self.raw_samples)
            self._update_dashboard()
            self._update_preview()
            self._draw_chart()
            self._log("Pipeline", "Info", "Preprocessing", "RunFullPipeline", "Signal preprocessing tugadi.", 0.10)
            self._set_status("Preprocessing tugadi", "good")
            self.txt_attack_report.setPlainText("Signal preprocessing bajarildi. Baseline yaratishga tayyor.")
        except Exception as ex:
            self._show_error(str(ex))

    def build_baseline(self) -> None:
        try:
            samples = self.processed_samples if self.processed_samples else self.raw_samples
            if not samples:
                raise ValueError("Baseline yaratish uchun sample yo‘q.")
            self.baseline_profile = self.pattern_learning_service.build_baseline_profile(samples)
            self._update_dashboard()
            self._log(
                "Baseline",
                "Info",
                "PatternLearning",
                "BuildBaseline",
                f"{self.baseline_profile.channel_count} kanal bo‘yicha normal profil yaratildi.",
                0.12,
            )
            self._set_status("Baseline tayyor", "good")
            self.txt_attack_report.setPlainText(
                f"BASELINE PROFILE\n{'=' * 50}\n"
                f"TotalSamples : {self.baseline_profile.total_samples}\n"
                f"ChannelCount : {self.baseline_profile.channel_count}\n"
                f"Labels       : {self.baseline_profile.label_distribution}\n\n"
                f"Endi attack detection ni ishlatishingiz mumkin."
            )
        except Exception as ex:
            self._show_error(str(ex))

    def detect_attack(self) -> None:
        try:
            samples = self.processed_samples if self.processed_samples else self.raw_samples
            if not samples:
                raise ValueError("Avval dataset yuklang.")
            if self.baseline_profile is None:
                raise ValueError("Avval baseline yarating.")
            channel_name = self.cmb_channel.currentText().strip()
            if not channel_name:
                raise ValueError("Kanal tanlanmagan.")
            self.attack_detection_result = self.attack_detection_service.analyze_channel(samples, self.baseline_profile, channel_name)
            result = self.attack_detection_result
            self.txt_attack_report.setPlainText(
                f"ATTACK DETECTION HISOBOTI\n{'=' * 60}\n"
                f"Channel         : {result.channel_name}\n"
                f"AttackType      : {result.attack_type}\n"
                f"IsAttack        : {'Ha' if result.is_attack else 'Yo‘q'}\n"
                f"Confidence      : {result.confidence:.2f}\n"
                f"RiskScore       : {result.risk_score:.2f}\n"
                f"Severity        : {result.severity}\n\n"
                f"Indicators:\n" + "\n".join(f"- {k}: {v:.2f}" for k, v in result.indicators.items()) + "\n\n"
                f"Izoh:\n{result.description}"
            )
            self._log(
                "AttackDetection",
                result.severity,
                result.channel_name or "AttackEngine",
                result.attack_type,
                result.description,
                result.risk_score,
            )
            self._set_status("Attack tahlil bajarildi", "danger" if result.is_attack else "good")
            self._update_dashboard()
        except Exception as ex:
            self._show_error(str(ex))

    def verify_intent(self) -> None:
        try:
            confidence = float(self.txt_intent_confidence.text().strip())
            self.intent_prediction = self.intent_verification_service.verify_intent(
                self.txt_predicted_intent.text(),
                self.txt_decoded_command.text(),
                self.txt_expected_action.text(),
                confidence,
            )
            r = self.intent_prediction
            self.txt_intent_report.setPlainText(
                f"INTENT VERIFICATION HISOBOTI\n{'=' * 60}\n"
                f"ExpectedIntent     : {r.expected_intent}\n"
                f"PredictedIntent    : {r.predicted_intent}\n"
                f"DecodedCommand     : {r.decoded_command}\n"
                f"CanonicalExpected  : {r.canonical_expected}\n"
                f"CanonicalPredicted : {r.canonical_predicted}\n"
                f"CanonicalDecoded   : {r.canonical_decoded}\n\n"
                f"IsMatch            : {'Ha' if r.is_match else 'Yo‘q'}\n"
                f"IsSuspicious       : {'Ha' if r.is_suspicious else 'Yo‘q'}\n"
                f"Confidence         : {r.confidence:.2f}\n"
                f"MismatchScore      : {r.mismatch_score:.2f}\n"
                f"HijackProbability  : {r.hijack_probability:.2f}\n"
                f"RecommendedAction  : {r.recommended_action}\n\n"
                f"Izoh:\n{r.description}"
            )
            self._log(
                "IntentVerification",
                "Yuqori" if r.is_suspicious else "Past",
                "IntentEngine",
                r.recommended_action,
                r.description,
                r.hijack_probability,
            )
            self._set_status("Intent verification bajarildi", "danger" if r.is_suspicious else "good")
            self._update_dashboard()
        except Exception as ex:
            self._show_error(str(ex))

    def apply_protection(self) -> None:
        try:
            self.protection_action = self.protection_service.decide_protection(
                self.attack_detection_result,
                self.intent_prediction,
            )
            a = self.protection_action
            self.txt_protection_report.setPlainText(
                f"PROTECTION ENGINE HISOBOTI\n{'=' * 60}\n"
                f"ActionType      : {a.action_type}\n"
                f"BlockCommand    : {'Ha' if a.block_command else 'Yo‘q'}\n"
                f"SafeMode        : {'Yoqilgan' if a.safe_mode_enabled else 'O‘chiq'}\n"
                f"RequireRecheck  : {'Ha' if a.require_recheck else 'Yo‘q'}\n"
                f"ShowAlert       : {'Ha' if a.show_alert else 'Yo‘q'}\n"
                f"UpdatedRisk     : {a.updated_risk_score:.2f}\n\n"
                f"AlertMessage:\n{a.alert_message}\n\n"
                f"Izoh:\n{a.reason}"
            )
            self._log(
                "ProtectionEngine",
                "Kritik" if a.safe_mode_enabled else ("O‘rta" if a.show_alert else "Past"),
                "ProtectionEngine",
                a.action_type,
                a.reason,
                a.updated_risk_score,
            )
            self._set_status(a.action_type, "danger" if a.show_alert else "good")
            self._update_dashboard()
            if a.show_alert:
                QMessageBox.warning(self, "Protection Alert", a.alert_message)
        except Exception as ex:
            self._show_error(str(ex))

    def export_logs(self) -> None:
        try:
            file_path, _ = QFileDialog.getSaveFileName(self, "Loglarni saqlash", "neuroshield_logs.csv", "CSV Files (*.csv)")
            if not file_path:
                return
            self.logging_service.export_to_csv(file_path)
            QMessageBox.information(self, "Export", "Loglar muvaffaqiyatli saqlandi.")
        except Exception as ex:
            self._show_error(str(ex))

    def reset_all(self) -> None:
        self.raw_samples.clear()
        self.processed_samples.clear()
        self.baseline_profile = None
        self.attack_detection_result = None
        self.intent_prediction = None
        self.protection_action = None
        self.current_file_path = ""
        self.logging_service.clear_logs()
        self.cmb_channel.clear()
        self.lst_preview.clear()
        self.tbl_logs.setRowCount(0)
        self.lbl_loaded_file.setText("Hozircha fayl yuklanmagan")
        self.txt_expected_action.setText("chapga yurish")
        self.txt_predicted_intent.setText("chapga yurish")
        self.txt_decoded_command.setText("o‘ngga yurish")
        self.txt_intent_confidence.setText("0.92")
        self.chart_widget.clear_signal()
        self._reset_views()
        self._set_status("Tayyor emas", "warning")

    def on_channel_changed(self, _: str) -> None:
        self._update_dashboard()
        self._update_preview()
        self._draw_chart()

    # =========================
    # Helpers
    # =========================

    def _fill_channel_combo(self) -> None:
        self.cmb_channel.clear()
        samples = self.processed_samples if self.processed_samples else self.raw_samples
        if not samples:
            return
        channel_names = list(samples[0].channels.keys())
        self.cmb_channel.addItems(channel_names)

    def _update_preview(self) -> None:
        self.lst_preview.clear()
        samples = self.processed_samples if self.processed_samples else self.raw_samples
        channel_name = self.cmb_channel.currentText().strip()
        if not samples or not channel_name:
            return
        for sample in samples[:60]:
            if channel_name in sample.channels:
                value = sample.channels[channel_name]
                item = QListWidgetItem(
                    f"#{sample.sample_index:04d} | {sample.timestamp.strftime('%H:%M:%S.%f')[:-3]} | {channel_name} = {value:.6f}"
                )
                self.lst_preview.addItem(item)

    def _draw_chart(self) -> None:
        samples = self.processed_samples if self.processed_samples else self.raw_samples
        channel_name = self.cmb_channel.currentText().strip()
        if not samples or not channel_name:
            self.chart_widget.clear_signal()
            self.lbl_chart_info.setText("Grafik ko‘rsatish uchun EEG fayl yuklang.")
            return
        values = [s.channels[channel_name] for s in samples if channel_name in s.channels]
        max_points = 400
        if len(values) > max_points:
            step = max(1, len(values) // max_points)
            values = values[::step]
        self.chart_widget.set_signal(values, channel_name)
        self.lbl_chart_info.setText(f"{channel_name} kanali bo‘yicha {len(values)} ta nuqta ko‘rsatilmoqda.")

    def _update_dashboard(self) -> None:
        samples = self.processed_samples if self.processed_samples else self.raw_samples
        total_channels = len(samples[0].channels) if samples else 0
        self.lbl_total_samples.setText(str(len(samples)))
        self.lbl_total_channels.setText(str(total_channels))
        self.lbl_selected_channel.setText(self.cmb_channel.currentText().strip() or "-")

        risk = 0.0
        if self.protection_action:
            risk = self.protection_action.updated_risk_score
        elif self.intent_prediction:
            risk = max(risk, self.intent_prediction.hijack_probability)
        elif self.attack_detection_result:
            risk = max(risk, self.attack_detection_result.risk_score)
        self.lbl_risk.setText(f"{risk:.2f}")

    def _reset_views(self) -> None:
        self.txt_attack_report.setPlainText("Attack detection hali bajarilmagan.")
        self.txt_intent_report.setPlainText("Intent verification hali bajarilmagan.")
        self.txt_protection_report.setPlainText("Protection engine hali bajarilmagan.")
        self._update_dashboard()

    def _set_status(self, text: str, level: str) -> None:
        self.lbl_status.setText(text)
        if level == "good":
            self.lbl_status.setObjectName("statusGood")
        elif level == "danger":
            self.lbl_status.setObjectName("statusDanger")
        else:
            self.lbl_status.setObjectName("statusWarning")
        self.lbl_status.style().unpolish(self.lbl_status)
        self.lbl_status.style().polish(self.lbl_status)

    def _log(self, event_type: str, severity: str, source: str, action: str, description: str, risk: float) -> None:
        log = SecurityEventLog(
            timestamp=datetime.now(),
            event_type=event_type,
            severity=severity,
            source=source,
            action_taken=action,
            description=description,
            risk_score=risk,
        )
        self.logging_service.add_log(log)
        self._refresh_logs_table()

    def _refresh_logs_table(self) -> None:
        logs = self.logging_service.get_all_logs()
        self.tbl_logs.setRowCount(len(logs))
        for row, log in enumerate(logs):
            values = [
                log.timestamp.strftime("%H:%M:%S"),
                log.event_type,
                log.severity,
                log.source,
                log.action_taken,
                f"{log.risk_score:.2f}",
            ]
            for col, value in enumerate(values):
                item = QTableWidgetItem(value)
                self.tbl_logs.setItem(row, col, item)
            self.tbl_logs.item(row, 5).setTextAlignment(Qt.AlignCenter)

    def _show_error(self, message: str) -> None:
        self._set_status("Xatolik yuz berdi", "danger")
        QMessageBox.critical(self, "Xatolik", message)

    def _get_sampling_rate(self) -> float:
        try:
            sampling_rate = float(self.txt_sampling_rate.text().strip())
        except ValueError:
            sampling_rate = 128.0
        if sampling_rate <= 0:
            sampling_rate = 128.0
        return sampling_rate

    @staticmethod
    def _lighter(color: str) -> str:
        q = QColor(color)
        return q.lighter(115).name()


def main() -> None:
    app = QApplication(sys.argv)
    window = NeuroShieldWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
