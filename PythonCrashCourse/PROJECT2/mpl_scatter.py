import matplotlib.pyplot as plt

x_values=range(1,1001)
y_values = [value ** 2 for value in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
#ax.scatter(x_values, y_values, s=10,c="red")
#ax.scatter(x_values, y_values, s=10,c=(0,0.8,0))
ax.scatter(x_values, y_values, s=10,c=y_values,cmap=plt.cm.Blues)

ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)
ax.tick_params(axis="both",which="major",labelsize=14)
ax.axis([0,1100,0,1100000])

plt.savefig("squares_plot.jpg",bbox_inches="tight")
plt.show()
