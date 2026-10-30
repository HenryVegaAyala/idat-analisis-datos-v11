import matplotlib.pyplot as plt

canales = ["Tienda", "Web", "App"]
ventas = [50, 30, 20]

plt.pie(ventas, labels=canales, colors=["red", "green", "blue"], autopct="%1.1f%%")
plt.title("Distribución de Ventas por Canal")
plt.show()