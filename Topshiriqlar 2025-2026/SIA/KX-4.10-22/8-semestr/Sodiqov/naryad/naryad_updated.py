
# coding: utf-8
import sys
import sqlite3
import random
import csv
from datetime import datetime, timedelta

from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QFrame,
    QFileDialog,
    QFormLayout,
    QGridLayout,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QSpinBox,
    QTableWidget,
    QTableWidgetItem,
    QTabWidget,
    QTextEdit,
    QVBoxLayout,
    QWidget,
    QHeaderView,
)

DB_NAME = "naryad_system.db"

DEFAULT_SECTIONS = [
    ("4/1", "Aloqa qo'shinlari TQM"),
    ("4/2", "Aloqa qo'shinlari TQM"),
    ("4/3", "Axborot texnologiyalari va sun'iy intellekt qo'shinlari TQM"),
    ("4/4", "Axborot texnologiyalari va sun'iy intellekt qo'shinlari TQM"),
    ("4/5", "Axborotlarni kriptografik himoyalash va maxfiylik rejimi TQM"),
    ("4/6", "Havo hujumidan mudofaa zenit-raketa qo'shinlari TQM"),
    ("4/7", "Havo hujumidan mudofaa radiotexnika qo'shinlari TQM"),
    ("4/8", "Radioelektron razvedka va kurash qo'shinlari TQM"),
    ("4/9", "DXX chegara qo'shinlari (intellektual tizimlar) TQM"),
    ("4/10", "Kiberxavfsizlik qo'shinlari TQM"),
    ("3/1", "Havo hujumidan mudofaa quruqlikdagi qo'shinlar TQM"),
    ("2/1", "Havo hujumidan mudofaa quruqlikdagi qo'shinlar TAKTIK QOMONDONLIK MUHANDISLIGI"),
]

DEFAULT_DUTY_TYPES = [
    {"name": "BDP", "category": "Asosiy", "required_count": 1, "officer_slots": 0, "guard_slots": 0, "count_in_score": 1, "pvo_only": 0, "from_non_duty_pool": 0},
    {"name": "QTX", "category": "Asosiy", "required_count": 1, "officer_slots": 0, "guard_slots": 0, "count_in_score": 1, "pvo_only": 0, "from_non_duty_pool": 0},
    {"name": "SHTABB", "category": "Asosiy", "required_count": 1, "officer_slots": 0, "guard_slots": 0, "count_in_score": 1, "pvo_only": 0, "from_non_duty_pool": 0},
    {"name": "O'QUV BINO", "category": "Asosiy", "required_count": 1, "officer_slots": 0, "guard_slots": 0, "count_in_score": 1, "pvo_only": 0, "from_non_duty_pool": 0},
    {"name": "HAVO KUZATUV POSTI", "category": "Asosiy", "required_count": 1, "officer_slots": 0, "guard_slots": 0, "count_in_score": 1, "pvo_only": 1, "from_non_duty_pool": 0},
    {"name": "KAZARMA 1-ETAJ", "category": "Kazarma", "required_count": 0, "officer_slots": 1, "guard_slots": 3, "count_in_score": 1, "pvo_only": 0, "from_non_duty_pool": 0},
    {"name": "KAZARMA 2-ETAJ", "category": "Kazarma", "required_count": 0, "officer_slots": 1, "guard_slots": 3, "count_in_score": 1, "pvo_only": 0, "from_non_duty_pool": 0},
    {"name": "KAZARMA 3-ETAJ", "category": "Kazarma", "required_count": 0, "officer_slots": 1, "guard_slots": 3, "count_in_score": 1, "pvo_only": 0, "from_non_duty_pool": 0},
    {"name": "O'T O'CHIRISH GURUHI", "category": "Maxsus", "required_count": 1, "officer_slots": 0, "guard_slots": 0, "count_in_score": 0, "pvo_only": 0, "from_non_duty_pool": 1},
    {"name": "KUCHAYTIRUVCHI JANGOVOR BO'LINMA", "category": "Maxsus", "required_count": 1, "officer_slots": 0, "guard_slots": 0, "count_in_score": 0, "pvo_only": 0, "from_non_duty_pool": 1},
    {"name": "ZAMICHEANIYA NAVBATI", "category": "Intizomiy", "required_count": 1, "officer_slots": 0, "guard_slots": 0, "count_in_score": 0, "pvo_only": 0, "from_non_duty_pool": 0},
    {"name": "NAVBATDAN TASHQARI NAVBAT", "category": "Intizomiy", "required_count": 1, "officer_slots": 0, "guard_slots": 0, "count_in_score": 0, "pvo_only": 0, "from_non_duty_pool": 0},
]

DEFAULT_STATUSES = [
    "Aktiv",
    "Kasal",
    "Olimpiada",
    "Kasbiy",
    "Komandirovka",
    "Stajirovka",
    "Otpuska",
    "Vaqtincha chiqarilgan",
]

def parse_date(value):
    if not value:
        return None
    return datetime.strptime(value, "%Y-%m-%d").date()

def format_date(value):
    return value.strftime("%Y-%m-%d")

def section_course_from_code(code: str) -> int:
    try:
        return int(str(code).split("/")[0])
    except Exception:
        return 0

def is_pvo_section(section_name: str) -> bool:
    return "Havo hujumidan mudofaa" in (section_name or "")

def normalize_text(value):
    return str(value or "").strip().lower()

class DatabaseManager:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self._init_db()
        self._migrate_db()
        self._seed_defaults()

    def connect(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _init_db(self):
        with self.connect() as conn:
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS sections (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    code TEXT NOT NULL UNIQUE,
                    name TEXT NOT NULL,
                    course_no INTEGER NOT NULL DEFAULT 0,
                    is_active INTEGER NOT NULL DEFAULT 1
                )
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS status_reasons (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE,
                    is_active INTEGER NOT NULL DEFAULT 1
                )
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS cadets (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    last_name TEXT NOT NULL,
                    first_name TEXT NOT NULL,
                    middle_name TEXT NOT NULL,
                    full_name TEXT NOT NULL,
                    section_id INTEGER NOT NULL,
                    status TEXT NOT NULL DEFAULT 'Aktiv',
                    total_duties INTEGER NOT NULL DEFAULT 0,
                    last_duty_date TEXT,
                    can_be_duty_officer INTEGER NOT NULL DEFAULT 0,
                    officer_only INTEGER NOT NULL DEFAULT 0,
                    can_be_guard INTEGER NOT NULL DEFAULT 1,
                    notes TEXT,
                    created_at TEXT NOT NULL,
                    updated_at TEXT,
                    FOREIGN KEY(section_id) REFERENCES sections(id)
                )
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS duty_types (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE,
                    category TEXT NOT NULL,
                    required_count INTEGER NOT NULL DEFAULT 1,
                    officer_slots INTEGER NOT NULL DEFAULT 0,
                    guard_slots INTEGER NOT NULL DEFAULT 0,
                    count_in_score INTEGER NOT NULL DEFAULT 1,
                    pvo_only INTEGER NOT NULL DEFAULT 0,
                    from_non_duty_pool INTEGER NOT NULL DEFAULT 0,
                    is_active INTEGER NOT NULL DEFAULT 1
                )
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS responsible_persons (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    full_name TEXT NOT NULL,
                    role TEXT NOT NULL,
                    phone TEXT,
                    is_active INTEGER NOT NULL DEFAULT 1
                )
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS duty_plans (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    plan_name TEXT NOT NULL,
                    start_date TEXT NOT NULL,
                    end_date TEXT NOT NULL,
                    created_at TEXT NOT NULL
                )
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS duty_assignments (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    plan_id INTEGER NOT NULL,
                    duty_date TEXT NOT NULL,
                    duty_type_id INTEGER NOT NULL,
                    cadet_id INTEGER NOT NULL,
                    responsible_person_id INTEGER,
                    slot_role TEXT NOT NULL DEFAULT 'ODDIY',
                    count_in_score INTEGER NOT NULL DEFAULT 1,
                    note TEXT,
                    score REAL,
                    is_manual INTEGER NOT NULL DEFAULT 0,
                    FOREIGN KEY(plan_id) REFERENCES duty_plans(id),
                    FOREIGN KEY(duty_type_id) REFERENCES duty_types(id),
                    FOREIGN KEY(cadet_id) REFERENCES cadets(id),
                    FOREIGN KEY(responsible_person_id) REFERENCES responsible_persons(id)
                )
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS audit_logs (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    entity_name TEXT NOT NULL,
                    entity_id INTEGER NOT NULL,
                    action_type TEXT NOT NULL,
                    old_value TEXT,
                    new_value TEXT,
                    reason TEXT,
                    changed_at TEXT NOT NULL
                )
            """)
            conn.commit()

    def _add_column_if_missing(self, table_name: str, column_name: str, ddl: str):
        with self.connect() as conn:
            cur = conn.cursor()
            existing = [row[1] for row in cur.execute(f"PRAGMA table_info({table_name})").fetchall()]
            if column_name not in existing:
                cur.execute(f"ALTER TABLE {table_name} ADD COLUMN {ddl}")
                conn.commit()

    def _migrate_db(self):
        self._add_column_if_missing("sections", "course_no", "course_no INTEGER NOT NULL DEFAULT 0")
        for col in [
            ("cadets", "updated_at", "updated_at TEXT"),
            ("cadets", "can_be_duty_officer", "can_be_duty_officer INTEGER NOT NULL DEFAULT 0"),
            ("cadets", "officer_only", "officer_only INTEGER NOT NULL DEFAULT 0"),
            ("cadets", "can_be_guard", "can_be_guard INTEGER NOT NULL DEFAULT 1"),
            ("cadets", "notes", "notes TEXT"),
            ("duty_types", "officer_slots", "officer_slots INTEGER NOT NULL DEFAULT 0"),
            ("duty_types", "guard_slots", "guard_slots INTEGER NOT NULL DEFAULT 0"),
            ("duty_types", "count_in_score", "count_in_score INTEGER NOT NULL DEFAULT 1"),
            ("duty_types", "pvo_only", "pvo_only INTEGER NOT NULL DEFAULT 0"),
            ("duty_types", "from_non_duty_pool", "from_non_duty_pool INTEGER NOT NULL DEFAULT 0"),
            ("duty_assignments", "slot_role", "slot_role TEXT NOT NULL DEFAULT 'ODDIY'"),
            ("duty_assignments", "count_in_score", "count_in_score INTEGER NOT NULL DEFAULT 1"),
        ]:
            self._add_column_if_missing(*col)
        with self.connect() as conn:
            cur = conn.cursor()
            section_rows = cur.execute("SELECT id, code FROM sections WHERE course_no = 0 OR course_no IS NULL").fetchall()
            for row in section_rows:
                cur.execute("UPDATE sections SET course_no = ? WHERE id = ?", (section_course_from_code(row["code"]), row["id"]))
            conn.commit()

    def _seed_defaults(self):
        with self.connect() as conn:
            cur = conn.cursor()
            for code, name in DEFAULT_SECTIONS:
                cur.execute("INSERT OR IGNORE INTO sections (code, name, course_no) VALUES (?, ?, ?)", (code, name, section_course_from_code(code)))
            for item in DEFAULT_DUTY_TYPES:
                cur.execute(
                    """
                    INSERT OR IGNORE INTO duty_types
                    (name, category, required_count, officer_slots, guard_slots, count_in_score, pvo_only, from_non_duty_pool)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        item["name"], item["category"], item["required_count"], item["officer_slots"],
                        item["guard_slots"], item["count_in_score"], item["pvo_only"], item["from_non_duty_pool"]
                    ),
                )
            for status in DEFAULT_STATUSES:
                cur.execute("INSERT OR IGNORE INTO status_reasons (name) VALUES (?)", (status,))
            conn.commit()

    def fetch_sections(self):
        with self.connect() as conn:
            return conn.execute("SELECT id, code, name, course_no, is_active FROM sections WHERE is_active=1 ORDER BY course_no, code").fetchall()

    def add_section(self, code, name):
        with self.connect() as conn:
            conn.execute("INSERT INTO sections (code, name, course_no) VALUES (?, ?, ?)", (code.strip(), name.strip(), section_course_from_code(code)))
            conn.commit()

    def fetch_status_reasons(self):
        with self.connect() as conn:
            return conn.execute("SELECT id, name FROM status_reasons WHERE is_active=1 ORDER BY name").fetchall()

    def add_status_reason(self, name):
        with self.connect() as conn:
            conn.execute("INSERT INTO status_reasons (name) VALUES (?)", (name.strip(),))
            conn.commit()

    def fetch_cadets(self, section_id=None):
        sql = """
            SELECT c.id, c.last_name, c.first_name, c.middle_name, c.full_name, c.status, c.total_duties,
                   c.last_duty_date, c.can_be_duty_officer, c.officer_only, c.can_be_guard, COALESCE(c.notes,'') AS notes,
                   s.code AS section_code, s.name AS section_name, s.id AS section_id, s.course_no
            FROM cadets c JOIN sections s ON s.id = c.section_id
        """
        params = []
        if section_id:
            sql += " WHERE c.section_id = ?"
            params.append(section_id)
        sql += " ORDER BY s.course_no, s.code, c.last_name, c.first_name"
        with self.connect() as conn:
            return conn.execute(sql, params).fetchall()

    def fetch_cadet_by_id(self, cadet_id):
        with self.connect() as conn:
            return conn.execute("SELECT * FROM cadets WHERE id = ?", (cadet_id,)).fetchone()

    def add_cadet(self, last_name, first_name, middle_name, section_id, status, can_be_duty_officer, officer_only, can_be_guard, notes):
        full_name = f"{last_name.strip()} {first_name.strip()} {middle_name.strip()}"
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with self.connect() as conn:
            conn.execute(
                """
                INSERT INTO cadets
                (last_name, first_name, middle_name, full_name, section_id, status, can_be_duty_officer, officer_only, can_be_guard, notes, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (last_name.strip(), first_name.strip(), middle_name.strip(), full_name, section_id, status, int(can_be_duty_officer), int(officer_only), int(can_be_guard), notes.strip(), now, now)
            )
            conn.commit()

    def update_cadet(self, cadet_id, last_name, first_name, middle_name, section_id, status, can_be_duty_officer, officer_only, can_be_guard, notes):
        full_name = f"{last_name.strip()} {first_name.strip()} {middle_name.strip()}"
        with self.connect() as conn:
            conn.execute(
                """
                UPDATE cadets
                SET last_name=?, first_name=?, middle_name=?, full_name=?, section_id=?, status=?, can_be_duty_officer=?, officer_only=?, can_be_guard=?, notes=?, updated_at=?
                WHERE id=?
                """,
                (last_name.strip(), first_name.strip(), middle_name.strip(), full_name, section_id, status, int(can_be_duty_officer), int(officer_only), int(can_be_guard), notes.strip(), datetime.now().strftime("%Y-%m-%d %H:%M:%S"), cadet_id)
            )
            conn.commit()

    def delete_cadet(self, cadet_id):
        with self.connect() as conn:
            conn.execute("DELETE FROM cadets WHERE id = ?", (cadet_id,))
            conn.commit()

    def bulk_add_cadets(self, section_id, raw_text, status="Aktiv"):
        lines = [line.strip() for line in raw_text.splitlines() if line.strip()]
        failed = []
        inserted = 0
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with self.connect() as conn:
            for line in lines:
                parts = line.split()
                if len(parts) < 3:
                    failed.append(line)
                    continue
                last_name = parts[0]
                first_name = parts[1]
                middle_name = " ".join(parts[2:])
                full_name = f"{last_name} {first_name} {middle_name}"
                conn.execute(
                    """
                    INSERT INTO cadets
                    (last_name, first_name, middle_name, full_name, section_id, status, can_be_duty_officer, officer_only, can_be_guard, notes, created_at, updated_at)
                    VALUES (?, ?, ?, ?, ?, ?, 0, 0, 1, '', ?, ?)
                    """,
                    (last_name, first_name, middle_name, full_name, section_id, status, now, now)
                )
                inserted += 1
            conn.commit()
        return inserted, failed

    def fetch_duty_types(self):
        with self.connect() as conn:
            return conn.execute(
                """
                SELECT id, name, category, required_count, officer_slots, guard_slots, count_in_score, pvo_only, from_non_duty_pool, is_active
                FROM duty_types WHERE is_active=1 ORDER BY category, name
                """
            ).fetchall()

    def add_duty_type(self, name, category, required_count, officer_slots, guard_slots, count_in_score, pvo_only, from_non_duty_pool):
        with self.connect() as conn:
            conn.execute(
                """
                INSERT INTO duty_types (name, category, required_count, officer_slots, guard_slots, count_in_score, pvo_only, from_non_duty_pool)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (name.strip(), category.strip(), int(required_count), int(officer_slots), int(guard_slots), int(count_in_score), int(pvo_only), int(from_non_duty_pool))
            )
            conn.commit()

    def fetch_responsible_persons(self):
        with self.connect() as conn:
            return conn.execute("SELECT id, full_name, role, phone, is_active FROM responsible_persons WHERE is_active=1 ORDER BY full_name").fetchall()

    def add_responsible_person(self, full_name, role, phone):
        with self.connect() as conn:
            conn.execute("INSERT INTO responsible_persons (full_name, role, phone) VALUES (?, ?, ?)", (full_name.strip(), role.strip(), phone.strip()))
            conn.commit()

    def fetch_section_by_id(self, section_id):
        with self.connect() as conn:
            return conn.execute("SELECT id, code, name, course_no, is_active FROM sections WHERE id = ?", (section_id,)).fetchone()

    def delete_section(self, section_id):
        with self.connect() as conn:
            row = conn.execute("SELECT id, code, name FROM sections WHERE id = ?", (section_id,)).fetchone()
            if not row:
                raise ValueError("Seksiya topilmadi.")
            usage = conn.execute("SELECT COUNT(*) FROM cadets WHERE section_id = ?", (section_id,)).fetchone()[0]
            if usage:
                raise ValueError("Bu seksiyaga kursantlar biriktirilgan. Avval kursantlarni boshqa seksiyaga o'tkazing yoki o'chiring.")
            conn.execute("UPDATE sections SET is_active = 0 WHERE id = ?", (section_id,))
            conn.commit()

    def fetch_status_reason_by_id(self, status_id):
        with self.connect() as conn:
            return conn.execute("SELECT id, name, is_active FROM status_reasons WHERE id = ?", (status_id,)).fetchone()

    def delete_status_reason(self, status_id):
        with self.connect() as conn:
            row = conn.execute("SELECT id, name FROM status_reasons WHERE id = ?", (status_id,)).fetchone()
            if not row:
                raise ValueError("Holat topilmadi.")
            if row["name"] == "Aktiv":
                raise ValueError("'Aktiv' holatini o'chirib bo'lmaydi.")
            usage = conn.execute("SELECT COUNT(*) FROM cadets WHERE status = ?", (row["name"],)).fetchone()[0]
            if usage:
                raise ValueError("Bu holatdan foydalanayotgan kursantlar bor. Avval ularning holatini o'zgartiring.")
            conn.execute("UPDATE status_reasons SET is_active = 0 WHERE id = ?", (status_id,))
            conn.commit()

    def fetch_duty_type_by_id(self, duty_type_id):
        with self.connect() as conn:
            return conn.execute(
                "SELECT id, name, category, required_count, officer_slots, guard_slots, count_in_score, pvo_only, from_non_duty_pool, is_active FROM duty_types WHERE id = ?",
                (duty_type_id,),
            ).fetchone()

    def delete_duty_type(self, duty_type_id):
        with self.connect() as conn:
            row = conn.execute("SELECT id FROM duty_types WHERE id = ?", (duty_type_id,)).fetchone()
            if not row:
                raise ValueError("Naryad turi topilmadi.")
            conn.execute("UPDATE duty_types SET is_active = 0 WHERE id = ?", (duty_type_id,))
            conn.commit()

    def fetch_responsible_person_by_id(self, person_id):
        with self.connect() as conn:
            return conn.execute("SELECT id, full_name, role, phone, is_active FROM responsible_persons WHERE id = ?", (person_id,)).fetchone()

    def delete_responsible_person(self, person_id):
        with self.connect() as conn:
            row = conn.execute("SELECT id FROM responsible_persons WHERE id = ?", (person_id,)).fetchone()
            if not row:
                raise ValueError("Javobgar shaxs topilmadi.")
            conn.execute("UPDATE responsible_persons SET is_active = 0 WHERE id = ?", (person_id,))
            conn.commit()

    def _recalculate_cadet_stats(self, conn, cadet_ids):
        changed_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for cadet_id in {int(c) for c in cadet_ids if c is not None}:
            row = conn.execute(
                """
                SELECT COUNT(*) AS total_count, MAX(duty_date) AS last_date
                FROM duty_assignments
                WHERE cadet_id = ? AND count_in_score = 1
                """,
                (cadet_id,),
            ).fetchone()
            conn.execute(
                "UPDATE cadets SET total_duties = ?, last_duty_date = ?, updated_at = ? WHERE id = ?",
                (int(row["total_count"] or 0), row["last_date"], changed_at, cadet_id),
            )

    def delete_assignment(self, assignment_id, reason):
        if not reason:
            raise ValueError("O'chirish sababini kiriting.")
        assignment = self.fetch_assignment_by_id(assignment_id)
        if not assignment:
            raise ValueError("Assignment topilmadi")
        changed_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        old_value = f"assignment_id={assignment['id']}, cadet_id={assignment['cadet_id']}, duty_date={assignment['duty_date']}, duty_type_id={assignment['duty_type_id']}"
        with self.connect() as conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM duty_assignments WHERE id = ?", (assignment_id,))
            self._recalculate_cadet_stats(conn, [assignment["cadet_id"]])
            cur.execute(
                "INSERT INTO audit_logs (entity_name, entity_id, action_type, old_value, new_value, reason, changed_at) VALUES ('duty_assignment', ?, 'DELETE', ?, '', ?, ?)",
                (assignment_id, old_value, reason.strip(), changed_at),
            )
            conn.commit()

    def delete_plan(self, plan_id, reason):
        if not reason:
            raise ValueError("Rejani o'chirish sababini kiriting.")
        with self.connect() as conn:
            cur = conn.cursor()
            plan = cur.execute("SELECT id, plan_name FROM duty_plans WHERE id = ?", (plan_id,)).fetchone()
            if not plan:
                raise ValueError("Reja topilmadi.")
            assignments = cur.execute("SELECT id, cadet_id FROM duty_assignments WHERE plan_id = ?", (plan_id,)).fetchall()
            cadet_ids = [row["cadet_id"] for row in assignments]
            cur.execute("DELETE FROM duty_assignments WHERE plan_id = ?", (plan_id,))
            cur.execute("DELETE FROM duty_plans WHERE id = ?", (plan_id,))
            self._recalculate_cadet_stats(conn, cadet_ids)
            cur.execute(
                "INSERT INTO audit_logs (entity_name, entity_id, action_type, old_value, new_value, reason, changed_at) VALUES ('duty_plan', ?, 'DELETE', ?, '', ?, ?)",
                (plan_id, f"plan_name={plan['plan_name']}", reason.strip(), datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
            )
            conn.commit()

    def fetch_top_cadets(self, limit=5):
        with self.connect() as conn:
            return conn.execute(
                """
                SELECT c.full_name, c.total_duties, COALESCE(c.last_duty_date, '-') AS last_duty_date, s.code AS section_code
                FROM cadets c
                JOIN sections s ON s.id = c.section_id
                ORDER BY c.total_duties DESC, c.full_name
                LIMIT ?
                """,
                (limit,),
            ).fetchall()

    def fetch_generation_candidates(self):
        with self.connect() as conn:
            return conn.execute(
                """
                SELECT c.id, c.full_name, c.section_id, s.code AS section_code, s.name AS section_name, s.course_no,
                       c.total_duties, c.last_duty_date, c.can_be_duty_officer, c.officer_only, c.can_be_guard
                FROM cadets c JOIN sections s ON s.id = c.section_id
                WHERE c.status='Aktiv'
                ORDER BY s.course_no, s.code, c.full_name
                """
            ).fetchall()

    def fetch_assigned_cadet_ids_by_date(self, start_date, end_date):
        result = {}
        with self.connect() as conn:
            rows = conn.execute("SELECT duty_date, cadet_id FROM duty_assignments WHERE duty_date BETWEEN ? AND ?", (start_date, end_date)).fetchall()
        for row in rows:
            result.setdefault(row["duty_date"], set()).add(row["cadet_id"])
        return result

    def save_duty_plan(self, plan_name, start_date, end_date, assignments):
        if not assignments:
            raise ValueError("Saqlash uchun assignment yo'q")
        created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cadet_summary = {}
        with self.connect() as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO duty_plans (plan_name, start_date, end_date, created_at) VALUES (?, ?, ?, ?)", (plan_name, start_date, end_date, created_at))
            plan_id = cur.lastrowid
            for item in assignments:
                cur.execute(
                    """
                    INSERT INTO duty_assignments
                    (plan_id, duty_date, duty_type_id, cadet_id, responsible_person_id, slot_role, count_in_score, note, score, is_manual)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """,
                    (
                        plan_id, item["duty_date"], item["duty_type_id"], item["cadet_id"], item.get("responsible_person_id"),
                        item.get("slot_role", "ODDIY"), int(item.get("count_in_score", 1)), item.get("note", ""), float(item.get("score", 0.0)), int(item.get("is_manual", 0))
                    )
                )
                if int(item.get("count_in_score", 1)) == 1:
                    cadet_id = item["cadet_id"]
                    cadet_summary.setdefault(cadet_id, {"count": 0, "last_date": item["duty_date"]})
                    cadet_summary[cadet_id]["count"] += 1
                    if item["duty_date"] > cadet_summary[cadet_id]["last_date"]:
                        cadet_summary[cadet_id]["last_date"] = item["duty_date"]
            for cadet_id, data in cadet_summary.items():
                cur.execute(
                    """
                    UPDATE cadets SET total_duties = total_duties + ?, last_duty_date = ?, updated_at = ?
                    WHERE id = ?
                    """,
                    (data["count"], data["last_date"], created_at, cadet_id)
                )
            conn.commit()

    def fetch_saved_plans(self):
        with self.connect() as conn:
            return conn.execute("SELECT id, plan_name, start_date, end_date, created_at FROM duty_plans ORDER BY id DESC").fetchall()

    def fetch_plan_assignments(self, plan_id):
        with self.connect() as conn:
            return conn.execute(
                """
                SELECT a.id, a.plan_id, a.duty_date, a.duty_type_id, a.cadet_id, a.responsible_person_id, a.slot_role,
                       a.count_in_score, COALESCE(a.note,'') AS note, a.score, a.is_manual,
                       d.name AS duty_name, d.pvo_only, d.from_non_duty_pool,
                       c.full_name, c.section_id,
                       s.code AS section_code, s.name AS section_name, s.course_no,
                       COALESCE(r.full_name,'-') AS responsible_name
                FROM duty_assignments a
                JOIN duty_types d ON d.id = a.duty_type_id
                JOIN cadets c ON c.id = a.cadet_id
                JOIN sections s ON s.id = c.section_id
                LEFT JOIN responsible_persons r ON r.id = a.responsible_person_id
                WHERE a.plan_id = ?
                ORDER BY a.duty_date, d.name, a.slot_role, c.full_name
                """,
                (plan_id,)
            ).fetchall()

    def fetch_assignment_by_id(self, assignment_id):
        with self.connect() as conn:
            return conn.execute(
                """
                SELECT a.*, d.name AS duty_name, d.pvo_only, d.from_non_duty_pool, c.full_name, c.section_id,
                       s.code AS section_code, s.name AS section_name
                FROM duty_assignments a
                JOIN duty_types d ON d.id = a.duty_type_id
                JOIN cadets c ON c.id = a.cadet_id
                JOIN sections s ON s.id = c.section_id
                WHERE a.id = ?
                """,
                (assignment_id,)
            ).fetchone()

    def fetch_cadets_assigned_on_plan_date(self, plan_id, duty_date, exclude_assignment_id=None):
        sql = "SELECT cadet_id FROM duty_assignments WHERE plan_id = ? AND duty_date = ?"
        params = [plan_id, duty_date]
        if exclude_assignment_id is not None:
            sql += " AND id <> ?"
            params.append(exclude_assignment_id)
        with self.connect() as conn:
            return {row["cadet_id"] for row in conn.execute(sql, params).fetchall()}

    def fetch_active_cadets_for_replacement(self):
        with self.connect() as conn:
            return conn.execute(
                """
                SELECT c.id, c.full_name, c.section_id, s.code AS section_code, s.name AS section_name, s.course_no,
                       c.total_duties, c.last_duty_date, c.can_be_duty_officer, c.officer_only, c.can_be_guard
                FROM cadets c JOIN sections s ON s.id = c.section_id
                WHERE c.status='Aktiv'
                ORDER BY s.course_no, s.code, c.full_name
                """
            ).fetchall()

    def update_assignment(self, assignment_id, new_cadet_id, new_responsible_person_id, new_note, reason):
        assignment = self.fetch_assignment_by_id(assignment_id)
        if not assignment:
            raise ValueError("Assignment topilmadi")
        changed_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        old_cadet_id = assignment["cadet_id"]
        new_cadet_id = int(new_cadet_id)
        old_value = f"cadet_id={assignment['cadet_id']}, responsible={assignment['responsible_person_id']}, note={assignment['note']}"
        new_value = f"cadet_id={new_cadet_id}, responsible={new_responsible_person_id}, note={new_note}"
        with self.connect() as conn:
            cur = conn.cursor()
            cur.execute(
                "UPDATE duty_assignments SET cadet_id=?, responsible_person_id=?, note=?, is_manual=1 WHERE id=?",
                (new_cadet_id, new_responsible_person_id, new_note.strip(), assignment_id),
            )
            if old_cadet_id != new_cadet_id and int(assignment["count_in_score"]) == 1:
                self._recalculate_cadet_stats(conn, [old_cadet_id, new_cadet_id])
            cur.execute(
                "INSERT INTO audit_logs (entity_name, entity_id, action_type, old_value, new_value, reason, changed_at) VALUES ('duty_assignment', ?, 'UPDATE', ?, ?, ?, ?)",
                (assignment_id, old_value, new_value, reason.strip(), changed_at),
            )
            conn.commit()

    def fetch_assignment_logs(self, assignment_id):
        with self.connect() as conn:
            return conn.execute(
                "SELECT action_type, old_value, new_value, reason, changed_at FROM audit_logs WHERE entity_name='duty_assignment' AND entity_id=? ORDER BY id DESC",
                (assignment_id,)
            ).fetchall()

    def count_summary(self):
        with self.connect() as conn:
            cur = conn.cursor()
            return {
                "sections": cur.execute("SELECT COUNT(*) FROM sections WHERE is_active=1").fetchone()[0],
                "cadets": cur.execute("SELECT COUNT(*) FROM cadets").fetchone()[0],
                "active_cadets": cur.execute("SELECT COUNT(*) FROM cadets WHERE status='Aktiv'").fetchone()[0],
                "duty_types": cur.execute("SELECT COUNT(*) FROM duty_types WHERE is_active=1").fetchone()[0],
                "responsible": cur.execute("SELECT COUNT(*) FROM responsible_persons WHERE is_active=1").fetchone()[0],
                "statuses": cur.execute("SELECT COUNT(*) FROM status_reasons WHERE is_active=1").fetchone()[0],
                "plans": cur.execute("SELECT COUNT(*) FROM duty_plans").fetchone()[0],
            }

# For syntax test we don't need UI classes below.


class DashboardTab(QWidget):
    def __init__(self, db):
        super().__init__()
        self.db = db
        self.labels = {}
        self._build_ui()
        self.refresh()

    def _build_ui(self):
        layout = QVBoxLayout(self)
        title = QLabel("Naryad boshqaruv tizimi — Control Center")
        title.setObjectName("pageTitle")
        subtitle = QLabel("Kursantlar, naryad turlari, javobgarlar, generator va saqlangan rejalar bitta joyda.")
        subtitle.setObjectName("pageSubtitle")
        layout.addWidget(title)
        layout.addWidget(subtitle)

        grid = QGridLayout()
        cards = [
            ("sections", "Seksiyalar"),
            ("cadets", "Jami kursantlar"),
            ("active_cadets", "Aktiv kursantlar"),
            ("duty_types", "Naryad yo'nalishlari"),
            ("responsible", "Javobgar shaxslar"),
            ("statuses", "Holat turlari"),
            ("plans", "Saqlangan rejalar"),
        ]
        row = col = 0
        for key, text_value in cards:
            box = QGroupBox(text_value)
            box.setObjectName("statCard")
            box_layout = QVBoxLayout(box)
            label = QLabel("0")
            label.setAlignment(Qt.AlignCenter)
            label.setObjectName("statValue")
            box_layout.addWidget(label)
            self.labels[key] = label
            grid.addWidget(box, row, col)
            col += 1
            if col == 3:
                row += 1
                col = 0
        layout.addLayout(grid)

        insight_box = QGroupBox("Tezkor ko'rinish")
        insight_layout = QVBoxLayout(insight_box)
        self.top_table = QTableWidget(0, 3)
        self.top_table.setHorizontalHeaderLabels(["Kursant", "Seksiya", "Jami naryad"])
        self.top_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.top_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.top_table.setSelectionBehavior(QTableWidget.SelectRows)
        insight_layout.addWidget(self.top_table)
        self.info = QLabel(
            "Yangi versiyada: tanlangan seksiya, holat, javobgar, naryad turi, reja va assignmentni o'chirish; qidiruv/filter; preview export; kuchliroq premium UI."
        )
        self.info.setWordWrap(True)
        self.info.setObjectName("infoBanner")
        insight_layout.addWidget(self.info)
        layout.addWidget(insight_box)
        layout.addStretch()

    def refresh(self):
        summary = self.db.count_summary()
        for key, value in summary.items():
            if key in self.labels:
                self.labels[key].setText(str(value))
        top_rows = self.db.fetch_top_cadets(5)
        self.top_table.setRowCount(len(top_rows))
        for i, row in enumerate(top_rows):
            self.top_table.setItem(i, 0, QTableWidgetItem(row["full_name"]))
            self.top_table.setItem(i, 1, QTableWidgetItem(row["section_code"]))
            self.top_table.setItem(i, 2, QTableWidgetItem(str(row["total_duties"])))


class SectionsTab(QWidget):
    def __init__(self, db, after_change_callback):
        super().__init__()
        self.db = db
        self.after_change_callback = after_change_callback
        self.selected_section_id = None
        self._build_ui()
        self.load_sections()

    def _build_ui(self):
        layout = QHBoxLayout(self)
        form_box = QGroupBox("Seksiyalarni boshqarish")
        form_layout = QFormLayout(form_box)
        self.code_input = QLineEdit()
        self.name_input = QLineEdit()
        self.selected_label = QLabel("Tanlangan seksiya: yo'q")
        save_btn = QPushButton("Saqlash")
        save_btn.clicked.connect(self.add_section)
        delete_btn = QPushButton("Tanlanganni o'chirish")
        delete_btn.clicked.connect(self.delete_section)
        clear_btn = QPushButton("Tozalash")
        clear_btn.clicked.connect(self.clear_form)
        form_layout.addRow("Seksiya kodi", self.code_input)
        form_layout.addRow("Seksiya nomi", self.name_input)
        form_layout.addRow(self.selected_label)
        btns = QHBoxLayout()
        for btn in [save_btn, delete_btn, clear_btn]:
            btns.addWidget(btn)
        form_layout.addRow(btns)

        self.table = QTableWidget(0, 4)
        self.table.setHorizontalHeaderLabels(["ID", "Kod", "Kurs", "Nomi"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.cellClicked.connect(self.on_row_selected)
        layout.addWidget(form_box, 1)
        layout.addWidget(self.table, 2)

    def load_sections(self):
        rows = self.db.fetch_sections()
        self.table.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, value in enumerate([str(row["id"]), row["code"], str(row["course_no"]), row["name"]]):
                self.table.setItem(i, j, QTableWidgetItem(value))

    def on_row_selected(self, row, _column):
        self.selected_section_id = int(self.table.item(row, 0).text())
        self.code_input.setText(self.table.item(row, 1).text())
        self.name_input.setText(self.table.item(row, 3).text())
        self.selected_label.setText(f"Tanlangan seksiya ID: {self.selected_section_id}")

    def add_section(self):
        code = self.code_input.text().strip()
        name = self.name_input.text().strip()
        if not code or not name:
            QMessageBox.warning(self, "Xatolik", "Seksiya kodi va nomini to'ldiring.")
            return
        try:
            self.db.add_section(code, name)
            self.clear_form()
            self.load_sections()
            self.after_change_callback()
        except sqlite3.IntegrityError:
            QMessageBox.warning(self, "Xatolik", "Bunday seksiya kodi allaqachon mavjud.")

    def delete_section(self):
        if self.selected_section_id is None:
            QMessageBox.warning(self, "Xatolik", "Avval seksiya tanlang.")
            return
        answer = QMessageBox.question(self, "Tasdiqlash", "Tanlangan seksiyani o'chirasizmi?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if answer != QMessageBox.Yes:
            return
        try:
            self.db.delete_section(self.selected_section_id)
            self.clear_form()
            self.load_sections()
            self.after_change_callback()
            QMessageBox.information(self, "Bajarildi", "Seksiya ro'yxatdan olib tashlandi.")
        except Exception as exc:
            QMessageBox.warning(self, "Xatolik", str(exc))

    def clear_form(self):
        self.selected_section_id = None
        self.code_input.clear()
        self.name_input.clear()
        self.selected_label.setText("Tanlangan seksiya: yo'q")
        self.table.clearSelection()


class StatusesTab(QWidget):
    def __init__(self, db, after_change_callback):
        super().__init__()
        self.db = db
        self.after_change_callback = after_change_callback
        self.selected_status_id = None
        self._build_ui()
        self.load_statuses()

    def _build_ui(self):
        layout = QHBoxLayout(self)
        form_box = QGroupBox("Holat/sabab boshqaruvi")
        form_layout = QFormLayout(form_box)
        self.status_name_input = QLineEdit()
        self.selected_label = QLabel("Tanlangan holat: yo'q")
        save_btn = QPushButton("Saqlash")
        save_btn.clicked.connect(self.add_status)
        delete_btn = QPushButton("Tanlanganni o'chirish")
        delete_btn.clicked.connect(self.delete_status)
        clear_btn = QPushButton("Tozalash")
        clear_btn.clicked.connect(self.clear_form)
        form_layout.addRow("Holat nomi", self.status_name_input)
        form_layout.addRow(self.selected_label)
        btns = QHBoxLayout()
        for btn in [save_btn, delete_btn, clear_btn]:
            btns.addWidget(btn)
        form_layout.addRow(btns)

        self.table = QTableWidget(0, 2)
        self.table.setHorizontalHeaderLabels(["ID", "Holat"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.cellClicked.connect(self.on_row_selected)
        layout.addWidget(form_box, 1)
        layout.addWidget(self.table, 2)

    def load_statuses(self):
        rows = self.db.fetch_status_reasons()
        self.table.setRowCount(len(rows))
        for i, row in enumerate(rows):
            self.table.setItem(i, 0, QTableWidgetItem(str(row["id"])))
            self.table.setItem(i, 1, QTableWidgetItem(row["name"]))

    def on_row_selected(self, row, _column):
        self.selected_status_id = int(self.table.item(row, 0).text())
        self.status_name_input.setText(self.table.item(row, 1).text())
        self.selected_label.setText(f"Tanlangan holat ID: {self.selected_status_id}")

    def add_status(self):
        name = self.status_name_input.text().strip()
        if not name:
            QMessageBox.warning(self, "Xatolik", "Holat nomini kiriting.")
            return
        try:
            self.db.add_status_reason(name)
            self.clear_form()
            self.load_statuses()
            self.after_change_callback()
        except sqlite3.IntegrityError:
            QMessageBox.warning(self, "Xatolik", "Bunday holat allaqachon mavjud.")

    def delete_status(self):
        if self.selected_status_id is None:
            QMessageBox.warning(self, "Xatolik", "Avval holat tanlang.")
            return
        answer = QMessageBox.question(self, "Tasdiqlash", "Tanlangan holatni o'chirasizmi?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if answer != QMessageBox.Yes:
            return
        try:
            self.db.delete_status_reason(self.selected_status_id)
            self.clear_form()
            self.load_statuses()
            self.after_change_callback()
            QMessageBox.information(self, "Bajarildi", "Holat ro'yxatdan olib tashlandi.")
        except Exception as exc:
            QMessageBox.warning(self, "Xatolik", str(exc))

    def clear_form(self):
        self.selected_status_id = None
        self.status_name_input.clear()
        self.selected_label.setText("Tanlangan holat: yo'q")
        self.table.clearSelection()


class CadetsTab(QWidget):
    def __init__(self, db, after_change_callback):
        super().__init__()
        self.db = db
        self.after_change_callback = after_change_callback
        self.selected_cadet_id = None
        self._build_ui()
        self.load_reference_data()
        self.load_cadets()

    def _build_ui(self):
        main_layout = QVBoxLayout(self)
        top_layout = QHBoxLayout()

        single_box = QGroupBox("Kursant qo'shish / tahrirlash")
        single_form = QFormLayout(single_box)
        self.last_name_input = QLineEdit()
        self.first_name_input = QLineEdit()
        self.middle_name_input = QLineEdit()
        self.section_combo = QComboBox()
        self.status_combo = QComboBox()
        self.can_officer_check = QCheckBox("Navbatchi bo'la oladi")
        self.officer_only_check = QCheckBox("Faqat navbatchi bo'ladi")
        self.can_guard_check = QCheckBox("Posbon / oddiy naryad bo'la oladi")
        self.can_guard_check.setChecked(True)
        self.notes_input = QTextEdit()
        self.notes_input.setFixedHeight(70)

        buttons = QHBoxLayout()
        add_btn = QPushButton("Yangi saqlash")
        add_btn.clicked.connect(self.add_cadet)
        update_btn = QPushButton("Tanlanganni yangilash")
        update_btn.clicked.connect(self.update_cadet)
        delete_btn = QPushButton("Tanlanganni o'chirish")
        delete_btn.clicked.connect(self.delete_cadet)
        clear_btn = QPushButton("Formani tozalash")
        clear_btn.clicked.connect(self.clear_form)
        for b in [add_btn, update_btn, delete_btn, clear_btn]:
            buttons.addWidget(b)

        self.selected_label = QLabel("Tanlangan kursant: yo'q")
        self.selected_label.setStyleSheet("color: #7f6000; font-weight: bold;")
        single_form.addRow("Familiya", self.last_name_input)
        single_form.addRow("Ism", self.first_name_input)
        single_form.addRow("Otasining ismi", self.middle_name_input)
        single_form.addRow("Seksiya", self.section_combo)
        single_form.addRow("Holat / sabab", self.status_combo)
        single_form.addRow(self.can_officer_check)
        single_form.addRow(self.officer_only_check)
        single_form.addRow(self.can_guard_check)
        single_form.addRow("Izoh", self.notes_input)
        single_form.addRow(self.selected_label)
        single_form.addRow(buttons)

        bulk_box = QGroupBox("Mass import")
        bulk_layout = QVBoxLayout(bulk_box)
        self.bulk_section_combo = QComboBox()
        self.bulk_status_combo = QComboBox()
        self.bulk_text = QTextEdit()
        self.bulk_text.setPlaceholderText("Har qatorda bitta FIO bo'lsin:\nAliyev Alisher Anvar o'g'li")
        bulk_save_btn = QPushButton("Mass qo'shish")
        bulk_save_btn.clicked.connect(self.bulk_add_cadets)
        bulk_layout.addWidget(QLabel("Seksiya"))
        bulk_layout.addWidget(self.bulk_section_combo)
        bulk_layout.addWidget(QLabel("Boshlang'ich holat"))
        bulk_layout.addWidget(self.bulk_status_combo)
        bulk_layout.addWidget(QLabel("FIO ro'yxati"))
        bulk_layout.addWidget(self.bulk_text)
        bulk_layout.addWidget(bulk_save_btn)

        top_layout.addWidget(single_box, 1)
        top_layout.addWidget(bulk_box, 1)
        main_layout.addLayout(top_layout)

        filter_layout = QHBoxLayout()
        filter_layout.addWidget(QLabel("Seksiya bo'yicha filter:"))
        self.filter_section_combo = QComboBox()
        self.filter_section_combo.currentIndexChanged.connect(self.load_cadets)
        filter_layout.addWidget(self.filter_section_combo)
        filter_layout.addWidget(QLabel("Qidiruv:"))
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("FIO, seksiya, holat yoki izoh bo'yicha qidiring...")
        self.search_input.textChanged.connect(self.load_cadets)
        filter_layout.addWidget(self.search_input)
        refresh_btn = QPushButton("Yangilash")
        refresh_btn.clicked.connect(self.load_cadets)
        filter_layout.addWidget(refresh_btn)
        filter_layout.addStretch()
        main_layout.addLayout(filter_layout)

        self.table = QTableWidget(0, 10)
        self.table.setHorizontalHeaderLabels(["ID", "FIO", "Kurs", "Seksiya", "Holat", "Jami naryad", "Oxirgi naryad", "Navbatchi", "Faqat navbatchi", "Posbon"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.cellClicked.connect(self.on_row_selected)
        main_layout.addWidget(self.table)

    def load_reference_data(self):
        sections = self.db.fetch_sections()
        statuses = self.db.fetch_status_reasons()
        for combo in [self.section_combo, self.bulk_section_combo, self.filter_section_combo]:
            combo.blockSignals(True)
            combo.clear()
            if combo == self.filter_section_combo:
                combo.addItem("Barchasi", None)
            for section in sections:
                combo.addItem(f"{section['code']} - {section['name']}", section["id"])
            combo.blockSignals(False)
        for combo in [self.status_combo, self.bulk_status_combo]:
            combo.clear()
            for status in statuses:
                combo.addItem(status["name"])

    def load_cadets(self):
        section_id = self.filter_section_combo.currentData() if self.filter_section_combo.count() else None
        rows = self.db.fetch_cadets(section_id)
        search_text = normalize_text(self.search_input.text()) if hasattr(self, "search_input") else ""
        if search_text:
            rows = [
                row for row in rows
                if search_text in normalize_text(row["full_name"])
                or search_text in normalize_text(row["section_code"])
                or search_text in normalize_text(row["status"])
                or search_text in normalize_text(row["notes"])
            ]
        self.table.setRowCount(len(rows))
        for i, row in enumerate(rows):
            values = [str(row["id"]), row["full_name"], str(row["course_no"]), row["section_code"], row["status"],
                      str(row["total_duties"]), row["last_duty_date"] or "-", "Ha" if int(row["can_be_duty_officer"]) else "Yo'q",
                      "Ha" if int(row["officer_only"]) else "Yo'q", "Ha" if int(row["can_be_guard"]) else "Yo'q"]
            for j, value in enumerate(values):
                self.table.setItem(i, j, QTableWidgetItem(value))

    def _find_combo_data(self, combo, value):
        for i in range(combo.count()):
            if combo.itemData(i) == value:
                combo.setCurrentIndex(i)
                return

    def _find_combo_text(self, combo, value):
        index = combo.findText(value, Qt.MatchFixedString)
        if index >= 0:
            combo.setCurrentIndex(index)

    def on_row_selected(self, row, _column):
        cadet_id = int(self.table.item(row, 0).text())
        cadet = self.db.fetch_cadet_by_id(cadet_id)
        self.selected_cadet_id = cadet_id
        self.last_name_input.setText(cadet["last_name"])
        self.first_name_input.setText(cadet["first_name"])
        self.middle_name_input.setText(cadet["middle_name"])
        self._find_combo_data(self.section_combo, cadet["section_id"])
        self._find_combo_text(self.status_combo, cadet["status"])
        self.can_officer_check.setChecked(bool(cadet["can_be_duty_officer"]))
        self.officer_only_check.setChecked(bool(cadet["officer_only"]))
        self.can_guard_check.setChecked(bool(cadet["can_be_guard"]))
        self.notes_input.setPlainText(cadet["notes"] or "")
        self.selected_label.setText(f"Tanlangan kursant ID: {cadet_id} | {cadet['full_name']}")

    def validate_form(self):
        last_name = self.last_name_input.text().strip()
        first_name = self.first_name_input.text().strip()
        middle_name = self.middle_name_input.text().strip()
        section_id = self.section_combo.currentData()
        status = self.status_combo.currentText().strip()
        notes = self.notes_input.toPlainText().strip()
        can_officer = self.can_officer_check.isChecked()
        officer_only = self.officer_only_check.isChecked()
        can_guard = self.can_guard_check.isChecked()
        if officer_only and not can_officer:
            QMessageBox.warning(self, "Xatolik", "Faqat navbatchi bo'ladigan kursantda 'Navbatchi bo'la oladi' belgilangan bo'lishi kerak.")
            return None
        if not last_name or not first_name or not middle_name or section_id is None or not status:
            QMessageBox.warning(self, "Xatolik", "Barcha maydonlarni to'ldiring.")
            return None
        return last_name, first_name, middle_name, section_id, status, can_officer, officer_only, can_guard, notes

    def add_cadet(self):
        values = self.validate_form()
        if not values:
            return
        self.db.add_cadet(*values)
        self.clear_form()
        self.load_cadets()
        self.after_change_callback()

    def update_cadet(self):
        if self.selected_cadet_id is None:
            QMessageBox.warning(self, "Xatolik", "Avval jadvaldan kursantni tanlang.")
            return
        values = self.validate_form()
        if not values:
            return
        self.db.update_cadet(self.selected_cadet_id, *values)
        self.clear_form()
        self.load_cadets()
        self.after_change_callback()
        QMessageBox.information(self, "Bajarildi", "Kursant ma'lumotlari yangilandi.")

    def delete_cadet(self):
        if self.selected_cadet_id is None:
            QMessageBox.warning(self, "Xatolik", "Avval jadvaldan kursantni tanlang.")
            return
        answer = QMessageBox.question(self, "Tasdiqlash", "Tanlangan kursantni o'chirishni tasdiqlaysizmi?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if answer == QMessageBox.Yes:
            self.db.delete_cadet(self.selected_cadet_id)
            self.clear_form()
            self.load_cadets()
            self.after_change_callback()

    def clear_form(self):
        self.selected_cadet_id = None
        self.last_name_input.clear()
        self.first_name_input.clear()
        self.middle_name_input.clear()
        self.notes_input.clear()
        self.can_officer_check.setChecked(False)
        self.officer_only_check.setChecked(False)
        self.can_guard_check.setChecked(True)
        if self.section_combo.count():
            self.section_combo.setCurrentIndex(0)
        if self.status_combo.count():
            self._find_combo_text(self.status_combo, "Aktiv")
        self.selected_label.setText("Tanlangan kursant: yo'q")
        self.table.clearSelection()

    def bulk_add_cadets(self):
        section_id = self.bulk_section_combo.currentData()
        status = self.bulk_status_combo.currentText().strip()
        raw_text = self.bulk_text.toPlainText().strip()
        if section_id is None or not raw_text or not status:
            QMessageBox.warning(self, "Xatolik", "Seksiya, holat va FIO ro'yxatini kiriting.")
            return
        inserted, failed = self.db.bulk_add_cadets(section_id, raw_text, status)
        self.bulk_text.clear()
        self.load_cadets()
        self.after_change_callback()
        message = f"{inserted} ta kursant qo'shildi."
        if failed:
            message += "\n\nQuyidagi qatorlar o'tkazib yuborildi:\n" + "\n".join(failed)
        QMessageBox.information(self, "Natija", message)


class DutyTypesTab(QWidget):
    def __init__(self, db, after_change_callback):
        super().__init__()
        self.db = db
        self.after_change_callback = after_change_callback
        self.selected_duty_type_id = None
        self._build_ui()
        self.load_duty_types()

    def _build_ui(self):
        layout = QHBoxLayout(self)
        form_box = QGroupBox("Naryad yo'nalishi qo'shish")
        form_layout = QFormLayout(form_box)
        self.name_input = QLineEdit()
        self.category_input = QLineEdit()
        self.required_count_spin = QSpinBox()
        self.required_count_spin.setRange(0, 100)
        self.required_count_spin.setValue(1)
        self.officer_slots_spin = QSpinBox()
        self.officer_slots_spin.setRange(0, 20)
        self.guard_slots_spin = QSpinBox()
        self.guard_slots_spin.setRange(0, 20)
        self.count_in_score_check = QCheckBox("Ballga qo'shilsin")
        self.count_in_score_check.setChecked(True)
        self.pvo_only_check = QCheckBox("Faqat PVO yo'nalishlari uchun")
        self.from_non_duty_pool_check = QCheckBox("Faqat shu kun naryadga tushmaganlardan tanlansin")
        self.selected_label = QLabel("Tanlangan naryad turi: yo'q")
        save_btn = QPushButton("Saqlash")
        save_btn.clicked.connect(self.add_duty_type)
        delete_btn = QPushButton("Tanlanganni o'chirish")
        delete_btn.clicked.connect(self.delete_duty_type)
        clear_btn = QPushButton("Tozalash")
        clear_btn.clicked.connect(self.clear_form)
        form_layout.addRow("Nomi", self.name_input)
        form_layout.addRow("Kategoriya", self.category_input)
        form_layout.addRow("Oddiy slot soni", self.required_count_spin)
        form_layout.addRow("Navbatchi sloti", self.officer_slots_spin)
        form_layout.addRow("Posbon sloti", self.guard_slots_spin)
        form_layout.addRow(self.count_in_score_check)
        form_layout.addRow(self.pvo_only_check)
        form_layout.addRow(self.from_non_duty_pool_check)
        form_layout.addRow(self.selected_label)
        btns = QHBoxLayout()
        for btn in [save_btn, delete_btn, clear_btn]:
            btns.addWidget(btn)
        form_layout.addRow(btns)

        self.table = QTableWidget(0, 9)
        self.table.setHorizontalHeaderLabels(["ID", "Nomi", "Kategoriya", "Oddiy", "Navbatchi", "Posbon", "Ball", "PVO", "Non-duty pool"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.cellClicked.connect(self.on_row_selected)
        layout.addWidget(form_box, 1)
        layout.addWidget(self.table, 2)

    def load_duty_types(self):
        rows = self.db.fetch_duty_types()
        self.table.setRowCount(len(rows))
        for i, row in enumerate(rows):
            values = [str(row["id"]), row["name"], row["category"], str(row["required_count"]), str(row["officer_slots"]), str(row["guard_slots"]),
                      "Ha" if int(row["count_in_score"]) else "Yo'q", "Ha" if int(row["pvo_only"]) else "Yo'q",
                      "Ha" if int(row["from_non_duty_pool"]) else "Yo'q"]
            for j, value in enumerate(values):
                self.table.setItem(i, j, QTableWidgetItem(value))

    def on_row_selected(self, row, _column):
        self.selected_duty_type_id = int(self.table.item(row, 0).text())
        duty = self.db.fetch_duty_type_by_id(self.selected_duty_type_id)
        if not duty:
            return
        self.name_input.setText(duty["name"])
        self.category_input.setText(duty["category"])
        self.required_count_spin.setValue(int(duty["required_count"]))
        self.officer_slots_spin.setValue(int(duty["officer_slots"]))
        self.guard_slots_spin.setValue(int(duty["guard_slots"]))
        self.count_in_score_check.setChecked(bool(duty["count_in_score"]))
        self.pvo_only_check.setChecked(bool(duty["pvo_only"]))
        self.from_non_duty_pool_check.setChecked(bool(duty["from_non_duty_pool"]))
        self.selected_label.setText(f"Tanlangan naryad turi ID: {self.selected_duty_type_id}")

    def add_duty_type(self):
        name = self.name_input.text().strip()
        category = self.category_input.text().strip()
        if not name or not category:
            QMessageBox.warning(self, "Xatolik", "Nomi va kategoriyani to'ldiring.")
            return
        try:
            self.db.add_duty_type(name, category, self.required_count_spin.value(), self.officer_slots_spin.value(),
                                  self.guard_slots_spin.value(), self.count_in_score_check.isChecked(),
                                  self.pvo_only_check.isChecked(), self.from_non_duty_pool_check.isChecked())
            self.clear_form()
            self.load_duty_types()
            self.after_change_callback()
        except sqlite3.IntegrityError:
            QMessageBox.warning(self, "Xatolik", "Bunday naryad yo'nalishi allaqachon mavjud.")

    def delete_duty_type(self):
        if self.selected_duty_type_id is None:
            QMessageBox.warning(self, "Xatolik", "Avval naryad turini tanlang.")
            return
        answer = QMessageBox.question(self, "Tasdiqlash", "Tanlangan naryad turini o'chirasizmi?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if answer != QMessageBox.Yes:
            return
        try:
            self.db.delete_duty_type(self.selected_duty_type_id)
            self.clear_form()
            self.load_duty_types()
            self.after_change_callback()
            QMessageBox.information(self, "Bajarildi", "Naryad turi faol ro'yxatdan olib tashlandi.")
        except Exception as exc:
            QMessageBox.warning(self, "Xatolik", str(exc))

    def clear_form(self):
        self.selected_duty_type_id = None
        self.name_input.clear()
        self.category_input.clear()
        self.required_count_spin.setValue(1)
        self.officer_slots_spin.setValue(0)
        self.guard_slots_spin.setValue(0)
        self.count_in_score_check.setChecked(True)
        self.pvo_only_check.setChecked(False)
        self.from_non_duty_pool_check.setChecked(False)
        self.selected_label.setText("Tanlangan naryad turi: yo'q")
        self.table.clearSelection()


class ResponsiblePersonsTab(QWidget):
    def __init__(self, db, after_change_callback):
        super().__init__()
        self.db = db
        self.after_change_callback = after_change_callback
        self.selected_responsible_id = None
        self._build_ui()
        self.load_responsibles()

    def _build_ui(self):
        layout = QHBoxLayout(self)
        form_box = QGroupBox("Javobgar shaxs qo'shish")
        form_layout = QFormLayout(form_box)
        self.full_name_input = QLineEdit()
        self.role_input = QLineEdit()
        self.phone_input = QLineEdit()
        self.selected_label = QLabel("Tanlangan javobgar: yo'q")
        save_btn = QPushButton("Saqlash")
        save_btn.clicked.connect(self.add_responsible)
        delete_btn = QPushButton("Tanlanganni o'chirish")
        delete_btn.clicked.connect(self.delete_responsible)
        clear_btn = QPushButton("Tozalash")
        clear_btn.clicked.connect(self.clear_form)
        form_layout.addRow("FIO", self.full_name_input)
        form_layout.addRow("Lavozim", self.role_input)
        form_layout.addRow("Telefon", self.phone_input)
        form_layout.addRow(self.selected_label)
        btns = QHBoxLayout()
        for btn in [save_btn, delete_btn, clear_btn]:
            btns.addWidget(btn)
        form_layout.addRow(btns)
        self.table = QTableWidget(0, 4)
        self.table.setHorizontalHeaderLabels(["ID", "FIO", "Lavozim", "Telefon"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.cellClicked.connect(self.on_row_selected)
        layout.addWidget(form_box, 1)
        layout.addWidget(self.table, 2)

    def load_responsibles(self):
        rows = self.db.fetch_responsible_persons()
        self.table.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, value in enumerate([str(row["id"]), row["full_name"], row["role"], row["phone"] or ""]):
                self.table.setItem(i, j, QTableWidgetItem(value))

    def on_row_selected(self, row, _column):
        self.selected_responsible_id = int(self.table.item(row, 0).text())
        person = self.db.fetch_responsible_person_by_id(self.selected_responsible_id)
        if not person:
            return
        self.full_name_input.setText(person["full_name"])
        self.role_input.setText(person["role"])
        self.phone_input.setText(person["phone"] or "")
        self.selected_label.setText(f"Tanlangan javobgar ID: {self.selected_responsible_id}")

    def add_responsible(self):
        full_name = self.full_name_input.text().strip()
        role = self.role_input.text().strip()
        phone = self.phone_input.text().strip()
        if not full_name or not role:
            QMessageBox.warning(self, "Xatolik", "FIO va lavozimni to'ldiring.")
            return
        self.db.add_responsible_person(full_name, role, phone)
        self.clear_form()
        self.load_responsibles()
        self.after_change_callback()

    def delete_responsible(self):
        if self.selected_responsible_id is None:
            QMessageBox.warning(self, "Xatolik", "Avval javobgar shaxs tanlang.")
            return
        answer = QMessageBox.question(self, "Tasdiqlash", "Tanlangan javobgar shaxsni o'chirasizmi?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if answer != QMessageBox.Yes:
            return
        try:
            self.db.delete_responsible_person(self.selected_responsible_id)
            self.clear_form()
            self.load_responsibles()
            self.after_change_callback()
            QMessageBox.information(self, "Bajarildi", "Javobgar shaxs faol ro'yxatdan olib tashlandi.")
        except Exception as exc:
            QMessageBox.warning(self, "Xatolik", str(exc))

    def clear_form(self):
        self.selected_responsible_id = None
        self.full_name_input.clear()
        self.role_input.clear()
        self.phone_input.clear()
        self.selected_label.setText("Tanlangan javobgar: yo'q")
        self.table.clearSelection()


class GeneratorTab(QWidget):
    def __init__(self, db, after_change_callback):
        super().__init__()
        self.db = db
        self.after_change_callback = after_change_callback
        self.preview_assignments = []
        self.preview_start_date = None
        self.preview_end_date = None
        self._build_ui()
        self.load_duty_rows()

    def _build_ui(self):
        main_layout = QVBoxLayout(self)
        header_box = QGroupBox("Naryad generator")
        header_layout = QFormLayout(header_box)
        self.plan_name_input = QLineEdit()
        self.start_date_edit = QDateEdit()
        self.start_date_edit.setCalendarPopup(True)
        self.start_date_edit.setDate(QDate.currentDate())
        self.end_date_edit = QDateEdit()
        self.end_date_edit.setCalendarPopup(True)
        self.end_date_edit.setDate(QDate.currentDate())
        self.cooldown_spin = QSpinBox()
        self.cooldown_spin.setRange(0, 30)
        self.cooldown_spin.setValue(5)
        header_layout.addRow("Reja nomi", self.plan_name_input)
        header_layout.addRow("Boshlanish sana", self.start_date_edit)
        header_layout.addRow("Tugash sana", self.end_date_edit)
        header_layout.addRow("Cooldown (kun)", self.cooldown_spin)
        main_layout.addWidget(header_box)

        self.duty_table = QTableWidget(0, 9)
        self.duty_table.setHorizontalHeaderLabels(["Tanlash", "Naryad", "Kategoriya", "Oddiy", "Navbatchi", "Posbon", "Ball", "PVO", "Javobgar"])
        self.duty_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.duty_table.verticalHeader().setVisible(False)
        main_layout.addWidget(self.duty_table)

        btn_layout = QHBoxLayout()
        for text, handler in [
            ("Avto generatsiya", self.generate_plan),
            ("Previewni bazaga saqlash", self.save_preview),
            ("Previewni CSV export", self.export_preview_csv),
            ("Yo'nalishlarni yangilash", self.load_duty_rows),
            ("Previewni tozalash", self.clear_preview),
        ]:
            btn = QPushButton(text)
            btn.clicked.connect(handler)
            btn_layout.addWidget(btn)
        btn_layout.addStretch()
        main_layout.addLayout(btn_layout)

        self.status_label = QLabel("Generatsiya hali bajarilmadi.")
        self.status_label.setWordWrap(True)
        self.status_label.setStyleSheet("padding: 8px; background: #fff2cc; border: 1px solid #f1c232;")
        main_layout.addWidget(self.status_label)

        self.preview_table = QTableWidget(0, 8)
        self.preview_table.setHorizontalHeaderLabels(["Sana", "Naryad", "Rol", "Kursant", "Seksiya", "Javobgar", "Izoh", "Score"])
        self.preview_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.preview_table.setEditTriggers(QTableWidget.NoEditTriggers)
        main_layout.addWidget(self.preview_table)

    def load_duty_rows(self):
        duties = self.db.fetch_duty_types()
        responsibles = self.db.fetch_responsible_persons()
        self.duty_table.setRowCount(len(duties))
        for row_idx, duty in enumerate(duties):
            check_item = QTableWidgetItem()
            check_item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
            check_item.setCheckState(Qt.Unchecked)
            self.duty_table.setItem(row_idx, 0, check_item)
            name_item = QTableWidgetItem(duty["name"])
            name_item.setData(Qt.UserRole, duty["id"])
            self.duty_table.setItem(row_idx, 1, name_item)
            self.duty_table.setItem(row_idx, 2, QTableWidgetItem(duty["category"]))
            self.duty_table.setItem(row_idx, 3, QTableWidgetItem(str(duty["required_count"])))
            self.duty_table.setItem(row_idx, 4, QTableWidgetItem(str(duty["officer_slots"])))
            self.duty_table.setItem(row_idx, 5, QTableWidgetItem(str(duty["guard_slots"])))
            self.duty_table.setItem(row_idx, 6, QTableWidgetItem("Ha" if int(duty["count_in_score"]) else "Yo'q"))
            self.duty_table.setItem(row_idx, 7, QTableWidgetItem("Ha" if int(duty["pvo_only"]) else "Yo'q"))
            responsible_combo = QComboBox()
            responsible_combo.addItem("Tanlanmagan", None)
            for person in responsibles:
                responsible_combo.addItem(f"{person['full_name']} ({person['role']})", person["id"])
            self.duty_table.setCellWidget(row_idx, 8, responsible_combo)

    def get_selected_duty_configs(self):
        configs = []
        all_duties = {d["id"]: d for d in self.db.fetch_duty_types()}
        for row in range(self.duty_table.rowCount()):
            check_item = self.duty_table.item(row, 0)
            if not check_item or check_item.checkState() != Qt.Checked:
                continue
            duty_id = self.duty_table.item(row, 1).data(Qt.UserRole)
            duty = all_duties[duty_id]
            configs.append({
                "duty_type_id": duty["id"], "duty_name": duty["name"], "required_count": duty["required_count"],
                "officer_slots": duty["officer_slots"], "guard_slots": duty["guard_slots"],
                "count_in_score": duty["count_in_score"], "pvo_only": duty["pvo_only"],
                "from_non_duty_pool": duty["from_non_duty_pool"],
                "responsible_person_id": self.duty_table.cellWidget(row, 8).currentData(),
                "responsible_name": self.duty_table.cellWidget(row, 8).currentText(),
            })
        configs.sort(key=lambda x: int(x["from_non_duty_pool"]))
        return configs

    def build_candidate_state(self):
        candidates = self.db.fetch_generation_candidates()
        state = {}
        section_active_counts = {}
        section_total_duties = {}
        for row in candidates:
            section_active_counts[row["section_id"]] = section_active_counts.get(row["section_id"], 0) + 1
            section_total_duties[row["section_id"]] = section_total_duties.get(row["section_id"], 0) + row["total_duties"]
            state[row["id"]] = {
                "id": row["id"], "full_name": row["full_name"], "section_id": row["section_id"], "section_code": row["section_code"],
                "section_name": row["section_name"], "course_no": row["course_no"], "total_duties": row["total_duties"],
                "last_duty_date": parse_date(row["last_duty_date"]), "can_be_duty_officer": int(row["can_be_duty_officer"]),
                "officer_only": int(row["officer_only"]), "can_be_guard": int(row["can_be_guard"]),
            }
        return state, section_active_counts, section_total_duties

    def _eligible_for_slot(self, cadet, slot_role, pvo_only):
        if pvo_only and not is_pvo_section(cadet["section_name"]):
            return False
        if slot_role == "NAVBATCHI":
            return cadet["can_be_duty_officer"] == 1
        if slot_role in ("POSBON", "ODDIY"):
            if cadet["officer_only"] == 1:
                return False
            return cadet["can_be_guard"] == 1
        return True

    def choose_best_candidate(self, candidate_state, assigned_for_day, current_date, cooldown_days, section_active_counts, section_total_duties, slot_role, pvo_only):
        primary_pool, fallback_pool = [], []
        for cadet in candidate_state.values():
            if cadet["id"] in assigned_for_day:
                continue
            if not self._eligible_for_slot(cadet, slot_role, pvo_only):
                continue
            if cadet["last_duty_date"] is None:
                days_since_last = 9999
            else:
                days_since_last = (current_date - cadet["last_duty_date"]).days
            active_count = max(section_active_counts.get(cadet["section_id"], 1), 1)
            section_ratio = section_total_duties.get(cadet["section_id"], 0) / active_count
            role_bonus = 5 if slot_role == "NAVBATCHI" and cadet["can_be_duty_officer"] == 1 else 0
            score = (days_since_last * 10.0) - (cadet["total_duties"] * 100.0) - (section_ratio * 20.0) + role_bonus + random.random()
            info = {"cadet": cadet, "score": round(score, 2)}
            fallback_pool.append(info)
            if cadet["last_duty_date"] is None or days_since_last > cooldown_days:
                primary_pool.append(info)
        if primary_pool:
            return max(primary_pool, key=lambda x: x["score"]), "OK"
        if fallback_pool:
            return max(fallback_pool, key=lambda x: x["score"]), "Cooldown buzildi"
        return None, "Nomzod topilmadi"

    def expand_slots(self, config):
        slots = []
        if int(config["officer_slots"]) > 0 or int(config["guard_slots"]) > 0:
            slots.extend(["NAVBATCHI"] * int(config["officer_slots"]))
            slots.extend(["POSBON"] * int(config["guard_slots"]))
        else:
            slots.extend(["ODDIY"] * int(config["required_count"]))
        return slots

    def generate_plan(self):
        start_date = self.start_date_edit.date().toPyDate()
        end_date = self.end_date_edit.date().toPyDate()
        cooldown_days = self.cooldown_spin.value()
        configs = self.get_selected_duty_configs()
        if start_date > end_date:
            QMessageBox.warning(self, "Xatolik", "Boshlanish sanasi tugash sanasidan katta bo'lmasligi kerak.")
            return
        if not configs:
            QMessageBox.warning(self, "Xatolik", "Kamida bitta naryad yo'nalishini belgilang.")
            return
        candidate_state, section_active_counts, section_total_duties = self.build_candidate_state()
        if not candidate_state:
            QMessageBox.warning(self, "Xatolik", "Generatsiya uchun Aktiv holatdagi kursant yo'q.")
            return
        assigned_by_date = self.db.fetch_assigned_cadet_ids_by_date(format_date(start_date), format_date(end_date))
        preview, warnings = [], []
        current_date = start_date
        while current_date <= end_date:
            day_key = format_date(current_date)
            assigned_for_day = set(assigned_by_date.get(day_key, set()))
            for config in configs:
                for slot_role in self.expand_slots(config):
                    chosen, status_note = self.choose_best_candidate(candidate_state, assigned_for_day, current_date, cooldown_days,
                                                                     section_active_counts, section_total_duties, slot_role, int(config["pvo_only"]) == 1)
                    if not chosen:
                        warnings.append(f"{day_key} | {config['duty_name']} | {slot_role} -> nomzod topilmadi")
                        continue
                    cadet = chosen["cadet"]
                    note = "" if status_note == "OK" else status_note
                    if status_note != "OK":
                        warnings.append(f"{day_key} | {config['duty_name']} | {cadet['full_name']} ({status_note})")
                    preview.append({
                        "duty_date": day_key, "duty_type_id": config["duty_type_id"], "duty_name": config["duty_name"], "cadet_id": cadet["id"],
                        "cadet_name": cadet["full_name"], "section_code": cadet["section_code"], "responsible_person_id": config["responsible_person_id"],
                        "responsible_name": config["responsible_name"], "slot_role": slot_role, "note": note, "score": chosen["score"],
                        "count_in_score": int(config["count_in_score"]), "is_manual": 0,
                    })
                    assigned_for_day.add(cadet["id"])
                    assigned_by_date[day_key] = assigned_for_day
                    if int(config["count_in_score"]) == 1:
                        cadet["total_duties"] += 1
                        cadet["last_duty_date"] = current_date
                        section_total_duties[cadet["section_id"]] = section_total_duties.get(cadet["section_id"], 0) + 1
            current_date += timedelta(days=1)
        self.preview_assignments = preview
        self.preview_start_date = format_date(start_date)
        self.preview_end_date = format_date(end_date)
        self.load_preview_table()
        summary = f"Preview tayyorlandi. Jami assignment: {len(preview)} ta."
        if warnings:
            summary += "\nOgohlantirishlar:\n- " + "\n- ".join(warnings[:25])
            if len(warnings) > 25:
                summary += f"\n... yana {len(warnings) - 25} ta ogohlantirish bor"
        else:
            summary += "\nCooldown buzilishi aniqlanmadi."
        self.status_label.setText(summary)

    def load_preview_table(self):
        self.preview_table.setRowCount(len(self.preview_assignments))
        for i, item in enumerate(self.preview_assignments):
            values = [item["duty_date"], item["duty_name"], item["slot_role"], item["cadet_name"], item["section_code"],
                      item["responsible_name"], item["note"], str(item["score"])]
            for j, value in enumerate(values):
                self.preview_table.setItem(i, j, QTableWidgetItem(value))

    def clear_preview(self):
        self.preview_assignments = []
        self.preview_start_date = None
        self.preview_end_date = None
        self.preview_table.setRowCount(0)
        self.status_label.setText("Preview tozalandi.")

    def export_preview_csv(self):
        if not self.preview_assignments:
            QMessageBox.warning(self, "Xatolik", "Avval preview generatsiya qiling.")
            return
        path, _ = QFileDialog.getSaveFileName(self, "Preview CSV eksport", "preview_assignments.csv", "CSV Files (*.csv)")
        if not path:
            return
        with open(path, "w", newline="", encoding="utf-8-sig") as f:
            writer = csv.writer(f)
            writer.writerow(["Sana", "Naryad", "Rol", "Kursant", "Seksiya", "Javobgar", "Ballga qo'shiladi", "Izoh", "Score"])
            for item in self.preview_assignments:
                writer.writerow([item["duty_date"], item["duty_name"], item["slot_role"], item["cadet_name"], item["section_code"], item["responsible_name"], "Ha" if int(item["count_in_score"]) else "Yo'q", item["note"], item["score"]])
        QMessageBox.information(self, "Bajarildi", "Preview CSV eksport qilindi.")

    def save_preview(self):
        if not self.preview_assignments:
            QMessageBox.warning(self, "Xatolik", "Saqlash uchun preview mavjud emas.")
            return
        plan_name = self.plan_name_input.text().strip() or f"Naryad reja {self.preview_start_date} dan {self.preview_end_date} gacha"
        self.db.save_duty_plan(plan_name, self.preview_start_date, self.preview_end_date, self.preview_assignments)
        QMessageBox.information(self, "Bajarildi", "Preview bazaga saqlandi.")
        self.clear_preview()
        self.after_change_callback()


class PlansTab(QWidget):
    def __init__(self, db, after_change_callback=None):
        super().__init__()
        self.db = db
        self.after_change_callback = after_change_callback
        self.selected_plan_id = None
        self.selected_assignment_id = None
        self.current_plan_name = ""
        self._build_ui()
        self.load_plans()

    def _build_ui(self):
        layout = QHBoxLayout(self)
        left_box = QGroupBox("Saqlangan rejalar")
        left_layout = QVBoxLayout(left_box)
        left_layout.addWidget(QLabel("Reja qidiruvi"))
        self.plan_search_input = QLineEdit()
        self.plan_search_input.setPlaceholderText("Reja nomi yoki sana bo'yicha qidiruv...")
        self.plan_search_input.textChanged.connect(self.load_plans)
        left_layout.addWidget(self.plan_search_input)
        refresh_btn = QPushButton("Rejalarni yangilash")
        refresh_btn.clicked.connect(self.load_plans)
        export_btn = QPushButton("Tanlangan rejani CSV export")
        export_btn.clicked.connect(self.export_plan_csv)
        delete_plan_btn = QPushButton("Tanlangan rejani o'chirish")
        delete_plan_btn.clicked.connect(self.delete_selected_plan)
        left_layout.addWidget(refresh_btn)
        left_layout.addWidget(export_btn)
        left_layout.addWidget(delete_plan_btn)
        self.plans_table = QTableWidget(0, 5)
        self.plans_table.setHorizontalHeaderLabels(["ID", "Nomi", "Boshlanish", "Tugash", "Yaratilgan"])
        self.plans_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.plans_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.plans_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.plans_table.cellClicked.connect(self.on_plan_selected)
        left_layout.addWidget(self.plans_table)

        right_box = QGroupBox("Reja assignmentlari va manual tahrirlash")
        right_layout = QVBoxLayout(right_box)
        self.plan_info_label = QLabel("Reja tanlanmagan.")
        self.plan_info_label.setWordWrap(True)
        right_layout.addWidget(self.plan_info_label)
        right_layout.addWidget(QLabel("Assignment qidiruvi"))
        self.assignment_search_input = QLineEdit()
        self.assignment_search_input.setPlaceholderText("Sana, naryad, kursant yoki seksiya bo'yicha qidiruv...")
        self.assignment_search_input.textChanged.connect(self.reload_current_plan)
        right_layout.addWidget(self.assignment_search_input)

        self.assignments_table = QTableWidget(0, 10)
        self.assignments_table.setHorizontalHeaderLabels(["ID", "Sana", "Naryad", "Rol", "Kursant", "Seksiya", "Javobgar", "Ball", "Manual", "Izoh"])
        self.assignments_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.assignments_table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.assignments_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.assignments_table.cellClicked.connect(self.on_assignment_selected)
        right_layout.addWidget(self.assignments_table)

        edit_box = QGroupBox("Tanlangan assignmentni tahrirlash")
        edit_form = QFormLayout(edit_box)
        self.assignment_target_label = QLabel("Assignment tanlanmagan.")
        self.replace_cadet_combo = QComboBox()
        self.replace_responsible_combo = QComboBox()
        self.replace_note_input = QTextEdit()
        self.replace_note_input.setFixedHeight(60)
        self.change_reason_input = QTextEdit()
        self.change_reason_input.setFixedHeight(60)
        update_btn = QPushButton("Almashtirish / yangilash")
        update_btn.clicked.connect(self.update_assignment)
        delete_assignment_btn = QPushButton("Tanlangan assignmentni o'chirish")
        delete_assignment_btn.clicked.connect(self.delete_selected_assignment)
        show_logs_btn = QPushButton("Tanlangan assignment loglarini ko'rsatish")
        show_logs_btn.clicked.connect(self.show_assignment_logs)
        edit_form.addRow(self.assignment_target_label)
        edit_form.addRow("Yangi kursant", self.replace_cadet_combo)
        edit_form.addRow("Yangi javobgar", self.replace_responsible_combo)
        edit_form.addRow("Izoh", self.replace_note_input)
        edit_form.addRow("O'zgartirish / o'chirish sababi", self.change_reason_input)
        edit_form.addRow(update_btn)
        edit_form.addRow(delete_assignment_btn)
        edit_form.addRow(show_logs_btn)
        right_layout.addWidget(edit_box)
        layout.addWidget(left_box, 1)
        layout.addWidget(right_box, 2)

    def load_plans(self):
        rows = self.db.fetch_saved_plans()
        search_text = normalize_text(self.plan_search_input.text()) if hasattr(self, "plan_search_input") else ""
        if search_text:
            rows = [
                row for row in rows
                if search_text in normalize_text(row["plan_name"])
                or search_text in normalize_text(row["start_date"])
                or search_text in normalize_text(row["end_date"])
                or search_text in normalize_text(row["created_at"])
            ]
        self.plans_table.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, value in enumerate([str(row["id"]), row["plan_name"], row["start_date"], row["end_date"], row["created_at"]]):
                self.plans_table.setItem(i, j, QTableWidgetItem(value))
        self.assignments_table.setRowCount(0)
        self.plan_info_label.setText("Reja tanlanmagan.")
        self.selected_plan_id = None
        self.selected_assignment_id = None
        self.current_plan_name = ""
        self.assignment_target_label.setText("Assignment tanlanmagan.")
        self.replace_cadet_combo.clear()
        self.replace_responsible_combo.clear()

    def _populate_assignments_table(self, rows):
        search_text = normalize_text(self.assignment_search_input.text()) if hasattr(self, "assignment_search_input") else ""
        if search_text:
            rows = [
                row for row in rows
                if search_text in normalize_text(row["duty_date"])
                or search_text in normalize_text(row["duty_name"])
                or search_text in normalize_text(row["slot_role"])
                or search_text in normalize_text(row["full_name"])
                or search_text in normalize_text(row["section_code"])
                or search_text in normalize_text(row["responsible_name"])
                or search_text in normalize_text(row["note"])
            ]
        self.assignments_table.setRowCount(len(rows))
        for i, item in enumerate(rows):
            values = [str(item["id"]), item["duty_date"], item["duty_name"], item["slot_role"], item["full_name"],
                      item["section_code"], item["responsible_name"], "Ha" if int(item["count_in_score"]) else "Yo'q",
                      "Ha" if int(item["is_manual"]) else "Yo'q", item["note"]]
            for j, value in enumerate(values):
                self.assignments_table.setItem(i, j, QTableWidgetItem(value))
        self.plan_info_label.setText(f"Tanlangan reja: {self.current_plan_name} | Ko'rsatilayotgan assignmentlar: {len(rows)} ta")

    def on_plan_selected(self, row, _column):
        self.selected_plan_id = int(self.plans_table.item(row, 0).text())
        self.current_plan_name = self.plans_table.item(row, 1).text()
        rows = self.db.fetch_plan_assignments(self.selected_plan_id)
        self._populate_assignments_table(rows)
        self.selected_assignment_id = None
        self.assignment_target_label.setText("Assignment tanlanmagan.")

    def on_assignment_selected(self, row, _column):
        assignment_id = int(self.assignments_table.item(row, 0).text())
        self.selected_assignment_id = assignment_id
        assignment = self.db.fetch_assignment_by_id(assignment_id)
        if not assignment:
            return
        self.assignment_target_label.setText(f"Tanlandi: {assignment['duty_date']} | {assignment['duty_name']} | {assignment['slot_role']} | {assignment['full_name']}")
        self.replace_note_input.setPlainText(assignment["note"] or "")
        self.change_reason_input.clear()
        self.load_replacement_candidates(assignment)
        self.load_responsible_combo(assignment["responsible_person_id"])

    def load_responsible_combo(self, selected_id):
        self.replace_responsible_combo.clear()
        self.replace_responsible_combo.addItem("Tanlanmagan", None)
        for person in self.db.fetch_responsible_persons():
            self.replace_responsible_combo.addItem(f"{person['full_name']} ({person['role']})", person["id"])
        for i in range(self.replace_responsible_combo.count()):
            if self.replace_responsible_combo.itemData(i) == selected_id:
                self.replace_responsible_combo.setCurrentIndex(i)
                break

    def load_replacement_candidates(self, assignment):
        occupied_ids = self.db.fetch_cadets_assigned_on_plan_date(assignment["plan_id"], assignment["duty_date"], exclude_assignment_id=assignment["id"])
        candidates = self.db.fetch_active_cadets_for_replacement()
        self.replace_cadet_combo.clear()
        for cadet in candidates:
            c = dict(cadet)
            if c["id"] in occupied_ids:
                continue
            if int(assignment["pvo_only"]) == 1 and not is_pvo_section(c["section_name"]):
                continue
            if assignment["slot_role"] == "NAVBATCHI" and int(c["can_be_duty_officer"]) != 1:
                continue
            if assignment["slot_role"] in ("POSBON", "ODDIY"):
                if int(c["officer_only"]) == 1 or int(c["can_be_guard"]) != 1:
                    continue
            label = f"{c['full_name']} | {c['section_code']} | jami:{c['total_duties']}"
            self.replace_cadet_combo.addItem(label, c["id"])
            if c["id"] == assignment["cadet_id"]:
                self.replace_cadet_combo.setCurrentIndex(self.replace_cadet_combo.count() - 1)

    def reload_current_plan(self):
        if self.selected_plan_id is None:
            return
        rows = self.db.fetch_plan_assignments(self.selected_plan_id)
        self._populate_assignments_table(rows)

    def update_assignment(self):
        if self.selected_assignment_id is None:
            QMessageBox.warning(self, "Xatolik", "Avval assignment tanlang.")
            return
        new_cadet_id = self.replace_cadet_combo.currentData()
        new_responsible_person_id = self.replace_responsible_combo.currentData()
        new_note = self.replace_note_input.toPlainText().strip()
        reason = self.change_reason_input.toPlainText().strip()
        if new_cadet_id is None:
            QMessageBox.warning(self, "Xatolik", "Yangi kursant tanlanmagan.")
            return
        if not reason:
            QMessageBox.warning(self, "Xatolik", "O'zgartirish sababini kiriting.")
            return
        try:
            self.db.update_assignment(self.selected_assignment_id, new_cadet_id, new_responsible_person_id, new_note, reason)
            QMessageBox.information(self, "Bajarildi", "Assignment yangilandi va log yozildi.")
            self.reload_current_plan()
        except Exception as exc:
            QMessageBox.warning(self, "Xatolik", str(exc))

    def delete_selected_assignment(self):
        if self.selected_assignment_id is None:
            QMessageBox.warning(self, "Xatolik", "Avval assignment tanlang.")
            return
        reason = self.change_reason_input.toPlainText().strip()
        if not reason:
            QMessageBox.warning(self, "Xatolik", "Assignmentni o'chirish sababi yozilishi kerak.")
            return
        answer = QMessageBox.question(self, "Tasdiqlash", "Tanlangan assignment o'chirilsinmi?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if answer != QMessageBox.Yes:
            return
        try:
            self.db.delete_assignment(self.selected_assignment_id, reason)
            self.selected_assignment_id = None
            self.assignment_target_label.setText("Assignment tanlanmagan.")
            self.reload_current_plan()
            if callable(self.after_change_callback):
                self.after_change_callback()
            QMessageBox.information(self, "Bajarildi", "Assignment o'chirildi.")
        except Exception as exc:
            QMessageBox.warning(self, "Xatolik", str(exc))

    def delete_selected_plan(self):
        if self.selected_plan_id is None:
            QMessageBox.warning(self, "Xatolik", "Avval reja tanlang.")
            return
        reason = self.change_reason_input.toPlainText().strip()
        if not reason:
            QMessageBox.warning(self, "Xatolik", "Rejani o'chirish sababi yozilishi kerak.")
            return
        answer = QMessageBox.question(self, "Tasdiqlash", "Tanlangan reja va uning barcha assignmentlari o'chirilsinmi?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if answer != QMessageBox.Yes:
            return
        try:
            self.db.delete_plan(self.selected_plan_id, reason)
            self.load_plans()
            if callable(self.after_change_callback):
                self.after_change_callback()
            QMessageBox.information(self, "Bajarildi", "Reja va assignmentlari o'chirildi.")
        except Exception as exc:
            QMessageBox.warning(self, "Xatolik", str(exc))

    def show_assignment_logs(self):
        if self.selected_assignment_id is None:
            QMessageBox.warning(self, "Xatolik", "Avval assignment tanlang.")
            return
        logs = self.db.fetch_assignment_logs(self.selected_assignment_id)
        if not logs:
            QMessageBox.information(self, "Log", "Bu assignment uchun log topilmadi.")
            return
        text_lines = []
        for item in logs[:10]:
            text_lines.append(
                f"{item['changed_at']}\n"
                f"Action: {item['action_type']}\n"
                f"Sabab: {item['reason']}\n"
                f"Eski: {item['old_value']}\n"
                f"Yangi: {item['new_value']}\n"
            )
        QMessageBox.information(self, "Assignment loglari", "\n----------------------\n".join(text_lines))

    def export_plan_csv(self):
        if self.selected_plan_id is None:
            QMessageBox.warning(self, "Xatolik", "Avval reja tanlang.")
            return
        rows = self.db.fetch_plan_assignments(self.selected_plan_id)
        if not rows:
            QMessageBox.warning(self, "Xatolik", "Eksport uchun assignment yo'q.")
            return
        path, _ = QFileDialog.getSaveFileName(self, "CSV eksport", f"plan_{self.selected_plan_id}.csv", "CSV Files (*.csv)")
        if not path:
            return
        with open(path, "w", newline="", encoding="utf-8-sig") as f:
            writer = csv.writer(f)
            writer.writerow(["Sana", "Naryad", "Rol", "Kursant", "Seksiya", "Javobgar", "Ballga qo'shiladi", "Izoh", "Score"])
            for item in rows:
                writer.writerow([item["duty_date"], item["duty_name"], item["slot_role"], item["full_name"], item["section_code"],
                                 item["responsible_name"], "Ha" if int(item["count_in_score"]) else "Yo'q", item["note"], round(item["score"], 2)])
        QMessageBox.information(self, "Bajarildi", "CSV export tayyorlandi.")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Naryad Boshqaruv Tizimi — Premium Edition")
        self.resize(1600, 940)
        self.db = DatabaseManager(DB_NAME)
        self._build_ui()

    def _build_ui(self):
        tabs = QTabWidget()
        self.dashboard_tab = DashboardTab(self.db)
        self.sections_tab = SectionsTab(self.db, self.refresh_all)
        self.statuses_tab = StatusesTab(self.db, self.refresh_all)
        self.cadets_tab = CadetsTab(self.db, self.refresh_all)
        self.duty_types_tab = DutyTypesTab(self.db, self.refresh_all)
        self.responsibles_tab = ResponsiblePersonsTab(self.db, self.refresh_all)
        self.generator_tab = GeneratorTab(self.db, self.refresh_all)
        self.plans_tab = PlansTab(self.db, self.refresh_all)
        tabs.addTab(self.dashboard_tab, "Dashboard")
        tabs.addTab(self.sections_tab, "Seksiyalar")
        tabs.addTab(self.statuses_tab, "Holatlar")
        tabs.addTab(self.cadets_tab, "Kursantlar")
        tabs.addTab(self.duty_types_tab, "Naryad turlari")
        tabs.addTab(self.responsibles_tab, "Javobgar shaxslar")
        tabs.addTab(self.generator_tab, "Naryad generator")
        tabs.addTab(self.plans_tab, "Saqlangan rejalar")

        root = QWidget()
        root_layout = QVBoxLayout(root)
        root_layout.setContentsMargins(14, 14, 14, 14)
        root_layout.setSpacing(12)

        hero = QFrame()
        hero.setObjectName("heroCard")
        hero_layout = QVBoxLayout(hero)
        hero_title = QLabel("NARYAD CONTROL CENTER")
        hero_title.setObjectName("heroTitle")
        hero_subtitle = QLabel(
            "Delete, search, premium UI, manual correction loglari, preview export va kuchliroq boshqaruv bitta oynada."
        )
        hero_subtitle.setObjectName("heroSubtitle")
        hero_layout.addWidget(hero_title)
        hero_layout.addWidget(hero_subtitle)
        root_layout.addWidget(hero)
        root_layout.addWidget(tabs)

        self.setCentralWidget(root)
        self.statusBar().showMessage("Tizim tayyor")

        self.setStyleSheet("""
            QWidget {
                font-size: 13px;
                color: #eaf2ff;
            }
            QMainWindow, QWidget#centralWidget {
                background: #0f172a;
            }
            QFrame#heroCard {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #1d4ed8, stop:1 #0f766e);
                border: 1px solid rgba(255,255,255,0.15);
                border-radius: 18px;
                padding: 10px;
            }
            QLabel#heroTitle {
                font-size: 26px;
                font-weight: 800;
                color: white;
            }
            QLabel#heroSubtitle {
                font-size: 13px;
                color: rgba(255,255,255,0.92);
            }
            QLabel#pageTitle {
                font-size: 20px;
                font-weight: 700;
                color: #f8fafc;
            }
            QLabel#pageSubtitle {
                color: #cbd5e1;
            }
            QLabel#statValue {
                font-size: 30px;
                font-weight: 800;
                color: #93c5fd;
            }
            QLabel#infoBanner {
                padding: 10px;
                border-radius: 10px;
                background: rgba(59,130,246,0.12);
                border: 1px solid rgba(147,197,253,0.30);
                color: #dbeafe;
            }
            QGroupBox {
                border: 1px solid rgba(148,163,184,0.25);
                border-radius: 16px;
                margin-top: 12px;
                padding-top: 10px;
                font-weight: 700;
                background: #111c34;
            }
            QGroupBox#statCard {
                background: #13203b;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 14px;
                padding: 0 6px;
                color: #f8fafc;
            }
            QPushButton {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #2563eb, stop:1 #0ea5e9);
                color: white;
                padding: 9px 14px;
                border-radius: 10px;
                border: none;
                font-weight: 700;
            }
            QPushButton:hover {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #1d4ed8, stop:1 #0284c7);
            }
            QPushButton:pressed {
                padding-top: 10px;
            }
            QLineEdit, QTextEdit, QComboBox, QSpinBox, QDateEdit, QTableWidget {
                background: #0b1222;
                color: #e2e8f0;
                border: 1px solid rgba(148,163,184,0.30);
                border-radius: 10px;
                padding: 7px;
                selection-background-color: #2563eb;
            }
            QHeaderView::section {
                background: #172554;
                color: #dbeafe;
                padding: 8px;
                border: none;
                border-right: 1px solid rgba(148,163,184,0.15);
            }
            QTableWidget {
                gridline-color: rgba(148,163,184,0.10);
                alternate-background-color: #111827;
            }
            QTabWidget::pane {
                border: 1px solid rgba(148,163,184,0.18);
                border-radius: 14px;
                background: #0b1222;
                top: -1px;
            }
            QTabBar::tab {
                background: #172554;
                color: #cbd5e1;
                padding: 11px 18px;
                margin-right: 4px;
                border-top-left-radius: 10px;
                border-top-right-radius: 10px;
            }
            QTabBar::tab:selected {
                background: #2563eb;
                color: white;
            }
            QScrollBar:vertical {
                background: #0b1222;
                width: 12px;
                margin: 0px;
            }
            QScrollBar::handle:vertical {
                background: #2563eb;
                min-height: 30px;
                border-radius: 6px;
            }
        """)

        for table in self.findChildren(QTableWidget):
            table.setAlternatingRowColors(True)
            table.verticalHeader().setDefaultSectionSize(28)

    def refresh_all(self):
        self.dashboard_tab.refresh()
        self.sections_tab.load_sections()
        self.statuses_tab.load_statuses()
        self.cadets_tab.load_reference_data()
        self.cadets_tab.load_cadets()
        self.duty_types_tab.load_duty_types()
        self.responsibles_tab.load_responsibles()
        self.generator_tab.load_duty_rows()
        self.plans_tab.load_plans()
        self.statusBar().showMessage("Ma'lumotlar yangilandi", 3000)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
