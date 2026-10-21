def calcular_igv(precio_base, igv=0.18):
    impuesto = precio_base * igv
    total = precio_base + impuesto

    return total

# Ejemplo de valor keyword
precio_c = calcular_igv(igv=0.19, precio_base=300)
print(f"Resultado con valor keyword: {precio_c}")

# Ejemplo con posicional
precio_a = calcular_igv(100, 0.17)
print(f"Resultado posicional: {precio_a}")

# Ejemplo de valor por defecto
precio_b = calcular_igv(200)
print(f"Resultado con valor por defecto: {precio_b}")
