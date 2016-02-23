from boids import update_boids, new_flock
from nose.tools import assert_almost_equal, assert_true
import os
import yaml
import numpy as np


def test_bad_boids_regression():
    regression_data = yaml.load(open(os.path.join(os.path.dirname(__file__), 'fixture.yml')))
    boid_data = regression_data["before"]
    update_boids(boid_data)
    for after, before in zip(regression_data["after"], boid_data):
        for after_value, before_value in zip(after, before):
            assert_almost_equal(after_value, before_value, delta=0.01)


def test_bad_boids_new_flock():
    window_data = yaml.load(open(os.path.join(os.path.dirname(__file__), 'myfile.yml')))
    windows = window_data['windows']
    counts = window_data['counts']
    for window in windows:
        for count in counts:
            points = new_flock(count, window[0], window[1])
            in_range = (points >= window[0]) * (points <= window[1])
            assert_true(np.all(in_range))
