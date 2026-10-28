import pandas as pd

df = pd.read_csv("ventas.csv")

resultado = df.drop(columns=["precio_unitario"])
print(resultado) # es una copia con la columna eliminada, no afecta el df original
print("-" * 100)

print(df.head()) # Es la data original, no se ha modificado
print("-" * 100)

resultado = df.drop(index=[2, 3])
print(resultado) # es una copia con la columna eliminada, no afecta el df original
