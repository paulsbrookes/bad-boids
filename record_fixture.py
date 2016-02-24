import yaml
from boids import new_flock, Flock
from copy import deepcopy
import numpy as np

flock = Flock()

before = np.copy([flock.positions, flock.velocities])
before = before.tolist()
flock.update_boids()
after = np.array([flock.positions, flock.velocities])
after = after.tolist()
fixture = {"before": before, "after": after}
fixture_file = open("update_fixture.yml", 'w')
fixture_file.write(yaml.dump(fixture))
fixture_file.close()

before = np.copy([flock.positions, flock.velocities])
before = before.tolist()
flock.move()
after = np.array([flock.positions, flock.velocities])
after = after.tolist()
fixture = {"before": before, "after": after}
fixture_file = open("move_fixture.yml", 'w')
fixture_file.write(yaml.dump(fixture))
fixture_file.close()
