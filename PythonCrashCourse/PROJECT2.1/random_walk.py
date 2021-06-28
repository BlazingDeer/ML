from random import choice


class RandomWalk:
    """Class to generate random walks."""

    def __init__(self, num_points=5000):
        """Initialize attributes of a walk."""
        self.num_points = num_points

        # all walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculate all the points in the walk."""

        while len(self.x_values) < self.num_points:
            # Decide which direction to go and how far to go in that direction
            x_step = self.get_step()

            y_step = self.get_step()

            if x_step == 0 and y_step == 0:
                continue

            # calculate the new postition.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

    def get_step(self, directions=[1, -1], distances=[0, 1, 2, 3, 4]):
        direction = choice(directions)
        distance = choice(distances)
        step = direction * distance
        return step