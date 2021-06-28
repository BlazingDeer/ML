from random_walk import RandomWalk
import matplotlib.pyplot as plt

# Make random walk.

while True:
    rw = RandomWalk(5000)
    rw.fill_walk()
    plt.style.use("classic")
    fig, ax = plt.subplots(figsize=(15, 9), dpi=91)
    ax.plot(rw.x_values, rw.y_values, linewidth=1)

    ax.scatter(0, 0, s=50, c="red", edgecolors="none")
    ax.scatter(rw.x_values[-1], rw.y_values[-1], s=50, c="red",
               edgecolors="none")
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)
    plt.show()
    keep_running = input("Make another walk?")
    if keep_running == "n":
        break
