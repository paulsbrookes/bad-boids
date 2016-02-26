from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import yaml
import os
from boids import Flock
from argparse import ArgumentParser

def process():
    parser = ArgumentParser(description="Boid simulation:simulates the \
     movement of birds using the Boid model.")
    parser.add_argument('--def_params', '-c', type=str, \
     default='default_fixture.yml',  help="File containing default parameters \
     for the boids simulation.")
    parser.add_argument('--boid_count', type=int, default=-1, required=False, \
     help="Specify the number of boids.")
    parser.add_argument('--attraction_strength', type=float, default=-1, \
     required=False, help="Specify the attraction strength between the boids.")
    parser.add_argument('--repulsion_distance', type=float, default=-1, \
     required=False, help="Specify the distance below which boids repel each \
      other.")
    parser.add_argument('--speed_match_strength', type=float, default=-1, \
     required=False, help="Specify the rate at which boids match their speeds.")
    parser.add_argument('--speed_match_distance', type=float, default=-1, \
     required=False, help="Specify the distance below which boids begin \
     # matching their speeds.")
    arguments = parser.parse_args()

    params = yaml.load(
        open(os.path.join(os.path.dirname(__file__), 'default_fixture.yml')))
    for arg in vars(arguments):
        if getattr(arguments, arg) != -1:
            params[arg] = getattr(arguments, arg)
    frames = params['frames']
    interval = params['interval']

    flock = Flock(
        boid_count=params['boid_count'],
        attraction_strength=params['attraction_strength'],
        repulsion_distance=params['repulsion_distance'],
        speed_match_distance=params['speed_match_distance'],
        speed_match_strength=params['speed_match_strength'],
        position_limits=params['position_limits'],
        velocity_limits=params['velocity_limits'])
    anim = animation.FuncAnimation(
    flock.figure, flock.animate, frames=frames, interval=interval)
    plt.show()

if __name__ == "__main__":
    process()
