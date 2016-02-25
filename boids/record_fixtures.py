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

before = np.copy([flock.positions, flock.velocities])
before = before.tolist()
flock.accelerate_to_middle()
after = np.array([flock.positions, flock.velocities])
after = after.tolist()
fixture = {"before": before, "after": after}
fixture_file = open("accelerate_to_middle_fixture.yml", 'w')
fixture_file.write(yaml.dump(fixture))
fixture_file.close()

before = np.copy([flock.positions, flock.velocities])
before = before.tolist()
flock.accelerate_from_boids()
after = np.array([flock.positions, flock.velocities])
after = after.tolist()
fixture = {"before": before, "after": after}
fixture_file = open("accelerate_from_boids_fixture.yml", 'w')
fixture_file.write(yaml.dump(fixture))
fixture_file.close()

before = np.copy([flock.positions, flock.velocities])
before = before.tolist()
flock.speed_match()
after = np.array([flock.positions, flock.velocities])
after = after.tolist()
fixture = {"before": before, "after": after}
fixture_file = open("speed_match_fixture.yml", 'w')
fixture_file.write(yaml.dump(fixture))
fixture_file.close()
