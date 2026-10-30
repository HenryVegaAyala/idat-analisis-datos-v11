import matplotlib.pyplot as plt

likes = [10, 50, 53, 100, 200, 500]
shares = [1, 5, 6, 10, 25, 60]

plt.scatter(likes, shares, color="purple", marker="D", s=200, alpha=0.5)

plt.title("Histograma de likes")
plt.xlabel("Likes")
plt.ylabel("Shares")
plt.grid()

plt.show()
