import matplotlib.pyplot as plt

# Datos de ejemplo
ciudades = ["Lima", "Arequipa", "Cusco"]
ventas = [500, 300, 450]

plt.bar(ciudades, ventas, color=["red", "blue", "#dd99ff"])

plt.title("Ventas por Ciudad")
plt.xlabel("Ciudad")
plt.ylabel("Ventas")

plt.grid(linestyle="--", alpha=0.5 , axis="y")

plt.show()
