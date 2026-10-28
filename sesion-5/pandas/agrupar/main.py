import pandas as pd

clientes = pd.read_csv("data/clientes.csv")
facturacion = pd.read_csv("data/facturacion.csv")

resultado = pd.merge(facturacion, clientes, on="id_cliente", how="inner")

consolidado = resultado[["id_factura", "nombre", "pais", "monto_total"]]

agrupado = consolidado.groupby("pais")["monto_total"].sum()
print(agrupado)

print("-" * 10)

agrupado = consolidado.groupby("pais")["monto_total"].agg(["sum", "mean", "max", "min"])
print(agrupado)

print("-" * 10)

agrupado = consolidado.groupby("pais").agg(
    ventas=("id_factura", "count"),
    ingreso=("monto_total", "sum")
).reset_index()
print(agrupado)