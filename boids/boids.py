from matplotlib import pyplot as plt
from matplotlib import animation
import random
import numpy as np
import yaml
import os

default_params = yaml.load(
        open(os.path.join(os.path.dirname(__file__), 'default_fixture.yml')))
def_position_limits = default_params['position_limits']
def_velocity_limits = default_params['velocity_limits']
boid_count = default_params['boid_count']
axes_limits = default_params['axes_limits']
frames = default_params['frames']
interval = default_params['interval']
def_movement_params = default_params['movement_params']

def new_flock(count, lower_limits, upper_limits):
    upper_limits = np.array(upper_limits)
    lower_limits = np.array(lower_limits)
    width = upper_limits - lower_limits
    difference = np.random.rand(lower_limits.size, count)*width[:, np.newaxis]
    return lower_limits[:, np.newaxis] + difference


class Flock(object):
    def __init__(self, position_limits=def_position_limits, velocity_limits=def_velocity_limits, boid_count=boid_count, movement_params=def_movement_params):
        self.positions = new_flock(boid_count, position_limits[0], position_limits[1])
        self.velocities = new_flock(boid_count, velocity_limits[0], velocity_limits[1])
        self.attraction_strength = movement_params[0]
        self.repulsion_distance = movement_params[1]
        self.speed_match_strength = movement_params[2]
        self.speed_match_distance = movement_params[3]
        self.figure = plt.figure()
        self.axes = plt.axes(xlim=axes_limits[0], ylim=axes_limits[1])
        self.scatter = self.axes.scatter(self.positions[:, 0], self.positions[:, 1])

    def update_boids(self):
        self.accelerate_to_middle()
        self.displacements_and_distances()
        self.accelerate_from_boids()
        self.speed_match()
        self.move()

    def accelerate_to_middle(self):
        middle = np.mean(self.positions, 1)
        direction_to_middle = middle[:, np.newaxis] - self.positions
        self.velocities += direction_to_middle*self.attraction_strength

    def displacements_and_distances(self):
        self.displacements = self.positions[:, np.newaxis, :] - self.positions[:, :, np.newaxis]
        squared_displacements = self.displacements ** 2
        self.square_distances = np.sum(squared_displacements, 0)

    def accelerate_from_boids(self):
        far_away = self.square_distances > self.repulsion_distance**2
        displacements_if_close = np.copy(self.displacements)
        displacements_if_close[0, :, :][far_away] = 0
        displacements_if_close[1, :, :][far_away] = 0
        self.velocities += np.sum(displacements_if_close, 1)

    def speed_match(self):
        velocity_differences = self.velocities[:, np.newaxis, :] - self.velocities[:, :, np.newaxis]
        very_far = self.square_distances > self.speed_match_distance**2
        velocity_differences_if_close = np.copy(velocity_differences)
        velocity_differences_if_close[0, :, :][very_far] = 0
        velocity_differences_if_close[1, :, :][very_far] = 0
        self.velocities -= (np.mean(velocity_differences_if_close, 1) * self.speed_match_strength)

    def move(self):
        self.positions += self.velocities

    def animate(self, frame):
        self.update_boids()
        self.scatter.set_offsets(zip(self.positions[0], self.positions[1]))
