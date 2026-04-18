import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from sklearn.linear_model import LinearRegression

# -----------------------
# 1. Dataset yaratish
# -----------------------
data = {
    'study_hours': [1, 2, 3, 4, 5, 6, 7, 8],
    'attendance': [50, 60, 65, 70, 75, 80, 90, 95],
    'score': [40, 45, 50, 60, 65, 70, 80, 90]
}

df = pd.DataFrame(data)

X = df[['study_hours', 'attendance']]
y = df['score']

# -----------------------
# 2. Modelni o‘rgatish
# -----------------------
model = LinearRegression()
model.fit(X, y)

# -----------------------
# 3. GUI yaratish
# -----------------------
class PredictorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Student Performance Predictor")

        self.label1 = QLabel("Study Hours:")
        self.input1 = QLineEdit()

        self.label2 = QLabel("Attendance (%):")
        self.input2 = QLineEdit()

        self.button = QPushButton("Predict")
        self.result = QLabel("Result: ")

        self.button.clicked.connect(self.predict_score)

        layout = QVBoxLayout()
        layout.addWidget(self.label1)
        layout.addWidget(self.input1)
        layout.addWidget(self.label2)
        layout.addWidget(self.input2)
        layout.addWidget(self.button)
        layout.addWidget(self.result)

        self.setLayout(layout)

    def predict_score(self):
        try:
            study_hours = float(self.input1.text())
            attendance = float(self.input2.text())

            prediction = model.predict([[study_hours, attendance]])
            score = round(prediction[0], 2)

            self.result.setText(f"Predicted Score: {score}")

        except:
            self.result.setText("Error: Enter valid numbers!")

# -----------------------
# 4. Run app
# -----------------------
app = QApplication(sys.argv)
window = PredictorApp()
window.show()
sys.exit(app.exec_())