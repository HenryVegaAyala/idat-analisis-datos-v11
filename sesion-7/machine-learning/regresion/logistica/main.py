import pandas as pd
from sklearn.linear_model import LogisticRegression

# Cargar los datos
df = pd.read_csv('datos_fuga.csv')

# Creación de variables
X = df[["antiguedad", "cuota_mensual"]]
y = df["fuga"]

# Crear el modelo de regresión lineal
modelo = LogisticRegression()
modelo.fit(X, y)

data_consulta = pd.DataFrame({"antiguedad": [3], "cuota_mensual": [50]})
resultado = modelo.predict(data_consulta)

print(modelo.coef_)
print(modelo.intercept_)
print(modelo.score(X, y))

print(f"El resultado de la predicción es: {resultado[0]}")
