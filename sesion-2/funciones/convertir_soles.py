def convertir_a_soles(dolares, cambio=3.80):
    return dolares * cambio


print(convertir_a_soles(100))
print(convertir_a_soles(100, 4.00))
print(convertir_a_soles(0))


def conversion_dolares(monto_soles, tipo_cambio=3.80):
    return monto_soles / tipo_cambio


print(conversion_dolares(380))
print(conversion_dolares(400, 4.00))
print(conversion_dolares(0))
