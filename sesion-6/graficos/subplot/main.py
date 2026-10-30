import matplotlib.pyplot as plt

plt.suptitle("Análisis de datos", fontsize=16, fontweight="bold")

plt.subplot(2, 2, 1)
plt.plot([1, 2, 3], [1, 4, 9])
plt.title('Gráfico 1')

plt.subplot(2, 2, 2)
plt.bar(['A', 'B', 'C'], [1, 2, 3])
plt.title('Gráfico 2')

plt.subplot(2, 2, 3)
plt.hist([1, 2, 3, 4, 5, 6], bins=5, edgecolor='black')
plt.title('Gráfico 3')

plt.subplot(2, 2, 4)
plt.scatter([1, 2, 3], [4, 5, 6])
plt.title('Gráfico 4')

plt.tight_layout()

plt.savefig("analisis_datos.png", dpi=300)

plt.show()
