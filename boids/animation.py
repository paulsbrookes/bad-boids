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
    parser.add_argument('--def_params', '-c', type=str, default='default_fixture.yml',  help="File containing default parameters for the boids simulation.")
    parser.add_argument('--boid_count', type=int, default=-1, required=False, help="Specify the number of boids.")
    parser.add_argument('--attraction_strength', type=float, default=-1, required=False, help="Specify the attraction strength between the boids.")
    parser.add_argument('--repulsion_distance', type=float,default=-1, required=False, help="Specify the distance below which boids repel each other.")
    parser.add_argument('--speed_match_strength', type=float,default=-1, required=False, help="Specify the rate at which boids match their speeds.")
    parser.add_argument('--speed_match_distance', type=float,default=-1, required=False, help="Specify the distance below which boids begin matching their speeds.")
    parser.add_argument('--position_limits', type=float,default=-1, required=False, help="Position limits. Specify [[xmin, ymin], [xmax, ymax]] for the initial random boid distribution.")
    parser.add_argument('--velocity_limits', type=float,default=-1, required=False, help="Velocitiy limits. Specify [[vxmin, vymin], [vxmax, vymax]] for the initial random boid distribution.")
    arguments = parser.parse_args()
    params = yaml.load(open('default_fixture.yml'))
    for arg in vars(arguments):
        if getattr(arguments, arg) != -1:
            params[arg] = getattr(arguments, arg)
    frames = params['frames']
    interval = params['interval']
    flock = Flock(boid_count=params['boid_count'])
    anim = animation.FuncAnimation(
    flock.figure, flock.animate, frames=frames, interval=interval)
    plt.show()

if __name__ == "__main__":
    process()

#boid_count=arguments.count, position_limits=arguments.position_limits, velocity_limits=arguments.velocity_limits, movement_params=[arguments.attraction_strength, arguments.repulsion_distance, arguments.speed_match_strength, arguments.speed_match_distance]
