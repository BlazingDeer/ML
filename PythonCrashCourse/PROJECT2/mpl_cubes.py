import matplotlib.pyplot as plt

x_vals = range(1, 5001)
y_vals = [value ** 3 for value in x_vals]

fig, ax = plt.subplots()
ax.scatter(x_vals, y_vals, s=5, c=y_vals, cmap=plt.cm.coolwarm)
ax.set_title("Cubes", fontsize=24)
ax.set_xlabel("Values", fontsize=14)
ax.set_ylabel("Cubes of values", fontsize=14)

ax.tick_params(axis="both", which="major", labelsize=10)

plt.show()
