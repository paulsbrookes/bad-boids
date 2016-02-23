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

boids = new_flock(boid_count, lower_limits, upper_limits)

def update_boids(boids):
	xs, ys, xvs, yvs = boids
	attraction_factor = 0.01/len(xs)

	# Fly towards the middle
	for i in range(len(xs)):  # repeated code
		for j in range(len(xs)):
			xvs[i] = xvs[i] + (xs[j] - xs[i]) * attraction_factor
	for i in range(len(xs)):
		for j in range(len(xs)):
			yvs[i]=yvs[i]+(ys[j]-ys[i])*attraction_factor
	# Fly away from nearby boids
	for i in range(len(xs)):
		for j in range(len(xs)):
			if (xs[j] - xs[i])**2 + (ys[j] - ys[i])**2 < 100:
				xvs[i] = xvs[i] + (xs[i] - xs[j])
				yvs[i] = yvs[i] + (ys[i] - ys[j])
	# Try to match speed with nearby boids
	for i in range(len(xs)):
		for j in range(len(xs)):
			if (xs[j] - xs[i])**2 + (ys[j]-ys[i])**2 < 10000:
				xvs[i] = xvs[i] + (xvs[j] - xvs[i])*0.125/len(xs)
				yvs[i] = yvs[i] + (yvs[j] - yvs[i])*0.125/len(xs)
	# Move according to velocities
	for i in range(len(xs)):
		xs[i] = xs[i] + xvs[i]
		ys[i] = ys[i] + yvs[i]


figure = plt.figure()
axes = plt.axes(xlim=(-500, 1500), ylim=(-500, 1500))
scatter = axes.scatter(boids[0], boids[1])

def animate(frame):
   update_boids(boids)
   scatter.set_offsets(zip(boids[0], boids[1]))


anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
