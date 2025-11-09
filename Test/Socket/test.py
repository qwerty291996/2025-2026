from sklearn.linear_model import LinearRegression
import numpy as np

# Uy ma'lumotlari (m²) va narxlari
x = np.array([[50], [70], [100]])  # maydon
y = np.array([40, 55, 80])         # narx (ming $)

# Model yaratamiz
model = LinearRegression()
model.fit(x, y)

# 90 m² uyning narxini taxmin qilamiz
prediction = model.predict([[90]])
print("Taxminiy narx:", round(prediction[0], 2), "ming $")
