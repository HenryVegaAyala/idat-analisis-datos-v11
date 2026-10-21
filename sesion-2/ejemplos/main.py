productos = ["Mouse", "Teclado", "Monitor"]
stock = [50, 20, 100]

# Sumatoria del stock total
stock_total = sum(stock)
print(f"La sumatoria del stock total es: {stock_total}")

# Producto con mayor stock
stock_maximo = max(stock) # Obtener el valor máximo del stock
print(f"El valor con mayor stock es: {stock_maximo}")

posicion_maximo = stock.index(stock_maximo) # Obtener la posición del valor máximo en la lista de stock
print(f"La posición del stock es: {posicion_maximo}")

producto = productos[posicion_maximo] # Obtener el nombre del producto con mayor stock usando la posición obtenida
print(f"El producto con mayor stock es: {producto}")