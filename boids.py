from matplotlib import pyplot as plt
from matplotlib import animation
import random
import numpy as np

boid_count = 50
lower_limits = np.array([-450, 50, 0, -20])
upper_limits = np.array([100, 1000, 10, 20])

def new_flock(count, lower_limits, upper_limits):
	width = upper_limits - lower_limits
	difference = np.random.rand(lower_limits.size, count)*width[:, np.newaxis]
	return lower_limits[:, np.newaxis] + difference

def update_boids(positions, velocities):
	xs, ys = positions
	xvs, yvs = velocities
	attraction_strength = 0.01
	repulsion_distance = 10
	speed_match_distance = 100
	speed_match_strength = 0.125

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

	#Move according to velocities
	positions += velocities

def animate(frame):
	update_boids(positions, velocities)
	scatter.set_offsets(zip(positions[0], positions[1]))


positions = new_flock(boid_count, lower_limits[0:2], upper_limits[0:2])
velocities = new_flock(boid_count, lower_limits[2:4], upper_limits[2:4])

figure = plt.figure()
axes = plt.axes(xlim=(-500, 1500), ylim=(-500, 1500))
scatter = axes.scatter(positions[0], positions[1])

anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
