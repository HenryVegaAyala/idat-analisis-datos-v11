import pandas as pd

clientes = pd.read_csv("data/clientes.csv")
pedidos = pd.read_csv("data/pedidos.csv")
productos = pd.read_csv("data/productos.csv")
categorias = pd.read_csv("data/categorias.csv")

resultado = pd.merge(pedidos, clientes, on="id_cliente", how="inner")
resultado = pd.merge(resultado, productos, on="id_producto", how="inner")
resultado = pd.merge(resultado, categorias, on="id_categoria", how="inner")

resultado["total"] = resultado["cantidad"] * resultado["precio"]

consolidado = resultado[["id_pedido", "nombre", "pais", "producto", "categoria", "cantidad", "total"]]

print(consolidado)
