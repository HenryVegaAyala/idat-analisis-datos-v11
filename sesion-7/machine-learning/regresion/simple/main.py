import pandas as pd
from sklearn.linear_model import LinearRegression

# Cargar los datos
df = pd.read_csv('datos_marketing.csv')

# Creación de variables
X = df[["marketing"]]
y = df["ventas"]

# Crear el modelo de regresión lineal
modelo = LinearRegression()
modelo.fit(X, y)

data_consulta = pd.DataFrame({"marketing": [6]})
resultado = modelo.predict(data_consulta)

print(modelo.coef_)
print(modelo.intercept_)
print(modelo.score(X, y))

print(f"El resultado de la predicción es: {resultado[0]}")