import matplotlib.pyplot as plt

# Datos de ejemplo
ciudades = ["Lima", "Arequipa", "Cusco"]
ventas = [500, 300, 450]

plt.bar(ciudades, ventas, color=["red", "blue", "#dd99ff"])

plt.title("Ventas por Ciudad")
plt.xlabel("Ciudad")
plt.ylabel("Ventas")

plt.grid(linestyle="--", alpha=0.3)

for x, y in zip(ciudades, ventas):
    plt.text(x, y + 5, str(y), va="center")

plt.tight_layout()
plt.show()
