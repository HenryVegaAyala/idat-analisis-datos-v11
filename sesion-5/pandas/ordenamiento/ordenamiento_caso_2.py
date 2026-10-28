import pandas as pd

df = pd.read_csv("ventas.csv")

# Ordenar por columna Producto de menos a mayor
o = df.sort_values("precio_unitario")

print(df.index[0:3].tolist()) # Me retorna valor como es sin orden

print((o.index[0:5].tolist())) # Me retorna el valor ordenado