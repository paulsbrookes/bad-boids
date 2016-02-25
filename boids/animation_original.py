from matplotlib import pyplot as plt
from matplotlib import animation
import random
import numpy as np
import yaml
import os
from boids import Flock

default_params = yaml.load(
        open(os.path.join(os.path.dirname(__file__), 'default_fixture.yml')))
frames = default_params['frames']
interval = default_params['interval']

flock = Flock()
fixture_file = open("original_fixture.yml", 'r')
fixture_data = yaml.load(fixture_file)
before = fixture_data["before"]
flock.positions = np.array([before[0], before[1]])
flock.velocities = np.array([before[2], before[3]])
fixture_file.close()



anim = animation.FuncAnimation(
 flock.figure, flock.animate, frames=frames, interval=interval)

if __name__ == "__main__":
    plt.show()
