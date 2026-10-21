import numpy as np

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

filtrado = np.array(lista)

resultado = filtrado[filtrado > 5]
print(filtrado > 5)
print(resultado)