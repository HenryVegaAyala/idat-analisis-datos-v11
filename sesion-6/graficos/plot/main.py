import matplotlib.pyplot as plt

horas = [1, 2, 3, 4]
tazas = [10, 20, 25, 30]

plt.plot(horas, tazas)
plt.title("Consumo de café por hora")
plt.xlabel("Horas")
plt.ylabel("Tazas de café")
plt.show()