import matplotlib.pyplot as plt

tienda_a = [100, 120, 130, 150, 170]
tienda_b = [90, 110, 140, 160, 180]

plt.plot(tienda_a, label="Tienda Norte")
plt.plot(tienda_b, label="Tienda Sur")

plt.title("Comparativa de tiendas")
plt.xlabel("Meses")
plt.ylabel("Ventas")

plt.legend()

plt.grid()

plt.show()