import yaml
from boids import new_flock, update_boids
from copy import deepcopy
import numpy as np

boid_count = 50
lower_limits = np.array([-450, 50, 0, -20])
upper_limits = np.array([100, 1000, 10, 20])
positions = new_flock(boid_count, lower_limits[0:2], upper_limits[0:2])
velocities = new_flock(boid_count, lower_limits[2:4], upper_limits[2:4])
before = np.copy([positions, velocities])
before = before.tolist()
update_boids(positions, velocities)
after = np.array([positions, velocities])
after = after.tolist()
fixture = {"before": before, "after": after}
fixture_file = open("fixture.yml", 'w')
fixture_file.write(yaml.dump(fixture))
fixture_file.close()
