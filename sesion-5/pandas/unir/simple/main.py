import pandas as pd

clientes = pd.read_csv("data/clientes.csv")
facturacion = pd.read_csv("data/facturacion.csv")

resultado = pd.merge(facturacion, clientes, on="id_cliente", how="inner")

consolidado = resultado[["id_factura", "nombre", "pais", "monto_total"]]

print(consolidado)