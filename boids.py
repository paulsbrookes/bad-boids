from matplotlib import pyplot as plt
from matplotlib import animation
import random
import numpy as np
import yaml
import os

default_params = yaml.load(
        open(os.path.join(os.path.dirname(__file__), 'default_fixture.yml')))
position_limits = np.array(default_params['position_limits'])
velocity_limits = np.array(default_params['velocity_limits'])
attraction_strength = default_params['attraction_strength']
repulsion_distance = default_params['repulsion_distance']
speed_match_distance = default_params['speed_match_distance']
speed_match_strength = default_params['speed_match_strength']
boid_count = default_params['boid_count']
axes_limits = default_params['axes_limits']
frames = default_params['frames']
interval = default_params['interval']


def new_flock(count, lower_limits, upper_limits):
    width = upper_limits - lower_limits
    difference = np.random.rand(lower_limits.size, count)*width[:, np.newaxis]
    return lower_limits[:, np.newaxis] + difference


class Flock(object):
    def __init__(self, default_params=default_params):
        self.positions = new_flock(
                            boid_count, position_limits[0], position_limits[1])
        self.velocities = new_flock(
                            boid_count, velocity_limits[0], velocity_limits[1])

    def update_boids(self):
        self.accelerate_to_middle()
        self.accelerate_from_boids()
        self.speed_match()
        self.move()

    def accelerate_to_middle(self):
        middle = np.mean(self.positions, 1)
        direction_to_middle = middle[:, np.newaxis] - self.positions
        self.velocities += direction_to_middle*attraction_strength

    def accelerate_from_boids(self):
        displacements = self.positions[:, np.newaxis, :] - self.positions[:, :, np.newaxis]
        squared_displacements = displacements ** 2
        self.square_distances = np.sum(squared_displacements, 0)
        far_away = self.square_distances > repulsion_distance ** 2
        displacements_if_close = np.copy(displacements)
        displacements_if_close[0, :, :][far_away] = 0
        displacements_if_close[1, :, :][far_away] = 0
        self.velocities += np.sum(displacements_if_close, 1)

    def speed_match(self):
        velocity_differences = self.velocities[:, np.newaxis, :] - self.velocities[:, :, np.newaxis]
        very_far = self.square_distances > speed_match_distance ** 2
        velocity_differences_if_close = np.copy(velocity_differences)
        velocity_differences_if_close[0, :, :][very_far] = 0
        velocity_differences_if_close[1, :, :][very_far] = 0
        self.velocities -= (np.mean(velocity_differences_if_close, 1) * speed_match_strength)

    def move(self):
        self.positions += self.velocities

    def animate(self, frame):
        self.update_boids()
        scatter.set_offsets(zip(self.positions[0], self.positions[1]))


flock = Flock()
figure = plt.figure()
axes = plt.axes(xlim=axes_limits[0], ylim=axes_limits[1])
scatter = axes.scatter(flock.positions[:, 0], flock.positions[:, 1])

anim = animation.FuncAnimation(
 figure, flock.animate, frames=frames, interval=interval)

if __name__ == "__main__":
    plt.show()
