import pandas as pd

df = pd.read_csv("ventas.csv")

# Ordenar por columna Producto de menos a mayor
menor_a_mayor = df.sort_values("producto")
print(menor_a_mayor)

print("*" * 100)

# Ordenar por columna Cantidad de mayor a menor
mayor_a_menor = df.sort_values("cantidad", ascending=False)
print(mayor_a_menor)

print("*" * 100)

# Ordenamiento multiple de producto y cantidad
ordenamiento_multiple = df.sort_values(["producto", "cantidad"], ascending=[True, False])
print(ordenamiento_multiple)
