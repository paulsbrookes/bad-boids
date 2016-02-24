"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import random
import numpy as np

# Deliberately terrible code for teaching purposes

boid_count = 50
lower_limits = np.array([-450, 50, 0, -20])
upper_limits = np.array([100, 1000, 10, 20])


def new_flock(count, lower_limits, upper_limits):
	width = upper_limits - lower_limits
	difference = np.random.rand(lower_limits.size, count)*width[:,np.newaxis]
	return lower_limits[:, np.newaxis] + difference

positions = new_flock(boid_count, lower_limits[0:2], upper_limits[0:2])
velocities = new_flock(boid_count, lower_limits[2:4], upper_limits[2:4])
#boids = new_flock(boid_count, lower_limits, upper_limits)

def update_boids(positions, velocities):
	xs, ys = positions
	xvs, yvs = velocities
	attraction_strength = 0.01
	repulsion_distance = 10
	speed_match_distance = 100
	speed_match_factor = 0.125/len(xs)
	middle = np.mean(positions, 1)
	direction_to_middle = middle[:,np.newaxis] - positions
	velocities += direction_to_middle*attraction_strength

	# Fly away from nearby boids
	for i in range(len(xs)):
		for j in range(len(xs)):
			if (xs[j] - xs[i])**2 + (ys[j] - ys[i])**2 < repulsion_distance**2:
				xvs[i] = xvs[i] + (xs[i] - xs[j])
				yvs[i] = yvs[i] + (ys[i] - ys[j])
	# Try to match speed with nearby boids
	for i in range(len(xs)):
		for j in range(len(xs)):
			if (xs[j] - xs[i])**2 + (ys[j]-ys[i])**2 < speed_match_distance**2:
				xvs[i] = xvs[i] + (xvs[j] - xvs[i])*speed_match_factor
				yvs[i] = yvs[i] + (yvs[j] - yvs[i])*speed_match_factor
	#Move according to velocities
	xs += xvs
	ys += yvs
	#print xs[0], ys[0], xvs[0], yvs[0]


figure = plt.figure()
axes = plt.axes(xlim = (-500, 1500), ylim = (-500, 1500))
scatter = axes.scatter(positions[0], positions[1])

def animate(frame):
   update_boids(positions, velocities)
   scatter.set_offsets(zip(positions[0], positions[1]))


anim = animation.FuncAnimation(figure, animate,
                               frames = 50, interval = 50)

if __name__ == "__main__":
    plt.show()
