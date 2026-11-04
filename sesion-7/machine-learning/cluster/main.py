import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv("datos_clientes.csv")

# Seleccionamos las columnas relevantes para el clustering
X = df[['gasto_anual', 'visitas_mes']]

# Creamos el modelo KMeans con 3 clusters
kmeans = KMeans(n_clusters=2, random_state=0)
# Ajustamos el modelo a los datos
kmeans.fit(X)

# Hacemos predicciones para nuevos clientes
bajo = pd.DataFrame({
    'gasto_anual': [50],
    'visitas_mes': [1]}
)

alto = pd.DataFrame({
    'gasto_anual': [1500],
    'visitas_mes': [8]}
)

print(f"Predicción para cliente con gasto anual de 50 y 1 visita al mes: {kmeans.predict(bajo)[0]}")
print(f"Predicción para cliente con gasto anual de 1500 y 8 visitas al mes: {kmeans.predict(alto)[0]}")
