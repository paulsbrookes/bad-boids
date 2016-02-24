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


def new_flock(count, lower_limits, upper_limits):
	width = upper_limits - lower_limits
	difference = np.random.rand(lower_limits.size, count)*width[:, np.newaxis]
	return lower_limits[:, np.newaxis] + difference


def update_boids(positions, velocities):
	# Move to middle
	middle = np.mean(positions, 1)
	direction_to_middle = middle[:, np.newaxis] - positions
	velocities += direction_to_middle*attraction_strength

	# Fly away from nearby boids
	displacements = positions[:, np.newaxis, :] - positions[:, :, np.newaxis]
	squared_displacements = displacements ** 2
	square_distances = np.sum(squared_displacements, 0)
	far_away = square_distances > repulsion_distance ** 2
	displacements_if_close = np.copy(displacements)
	displacements_if_close[0, :, :][far_away] = 0
	displacements_if_close[1, :, :][far_away] = 0
	velocities += np.sum(displacements_if_close, 1)

	# Try to match speed with nearby boids
	velocity_differences = velocities[:, np.newaxis, :] - velocities[:, :, np.newaxis]
	very_far = square_distances > speed_match_distance ** 2
	velocity_differences_if_close = np.copy(velocity_differences)
	velocity_differences_if_close[0, :, :][very_far] = 0
	velocity_differences_if_close[1, :, :][very_far] = 0
	velocities -= np.mean(velocity_differences_if_close, 1) * speed_match_strength

	# Move according to velocities
	positions += velocities


def animate(frame):
	update_boids(positions, velocities)
	scatter.set_offsets(zip(positions[0], positions[1]))


positions = new_flock(boid_count, position_limits[0], position_limits[1])
velocities = new_flock(boid_count, velocity_limits[0], velocity_limits[1])

figure = plt.figure()
axes = plt.axes(xlim=(-500, 1500), ylim=(-500, 1500))
scatter = axes.scatter(positions[0], positions[1])

anim = animation.FuncAnimation(figure, animate, frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
