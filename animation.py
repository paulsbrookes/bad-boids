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
anim = animation.FuncAnimation(
 flock.figure, flock.animate, frames=frames, interval=interval)

if __name__ == "__main__":
    plt.show()
