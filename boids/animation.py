from matplotlib import pyplot as plt
from matplotlib import animation
import random
import numpy as np
import yaml
import os
from boids import Flock
from argparse import ArgumentParser

def process():
    parser = ArgumentParser(description="Boid simulation: simulates the movement of birds using the Boid model.")
    parser.add_argument('--def_params', '-c', type=str, default="default_fixture.yml",  help="File containing default parameters for the boids simulation.")
    arguments = parser.parse_args()
    def_params = yaml.load(open(arguments.def_params))
    parser.add_argument('--count', type=int, default=def_params['boid_count'], required=False, help="Specify the number of boids.")
    parser.add_argument('--attraction_strength', type=float, default=def_params['movement_params'][0], required=False, help="Specify the attraction strength between the boids.")
    parser.add_argument('--repulsion_distance', type=float,default=def_params['movement_params'][1], required=False, help="Specify the distance below which boids repel each other.")
    parser.add_argument('--speed_match_strength', type=float,default=def_params['movement_params'][2], required=False, help="Specify the rate at which boids match their speeds.")
    parser.add_argument('--speed_match_distance', type=float,default=def_params['movement_params'][3], required=False, help="Specify the distance below which boids begin matching their speeds.")
    arguments = parser.parse_args()

    frames = def_params['frames']
    interval = def_params['interval']
    flock = Flock(boid_count=arguments.count, movement_params=[arguments.attraction_strength, arguments.repulsion_distance, arguments.speed_match_strength, arguments.speed_match_distance])
    anim = animation.FuncAnimation(
    flock.figure, flock.animate, frames=frames, interval=interval)
    plt.show()

if __name__ == "__main__":
    process()
