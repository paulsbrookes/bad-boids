from boids import update_boids, new_flock
from nose.tools import assert_almost_equal, assert_true
import os
import yaml
import numpy as np


def test_bad_boids_regression():
    regression_data = yaml.load(
        open(os.path.join(os.path.dirname(__file__), 'fixture.yml')))
    boid_data = np.array(regression_data["before"])
    update_boids(boid_data[0:2], boid_data[2:4])
    for after, before in zip(regression_data["after"], boid_data):
        for after_value, before_value in zip(after, before):
            assert_almost_equal(after_value, before_value, delta=0.01)


def test_bad_boids_new_flock():
    window_data = yaml.load(
        open(os.path.join(os.path.dirname(__file__), 'fixture.yml')))
    windows = window_data['windows']
    counts = window_data['counts']
    for window in windows:
        for count in counts:
            points = new_flock(count, np.array([window[0]]), np.array([window[1]]))
            in_range = (points >= window[0]) * (points <= window[1])
            assert_true(np.all(in_range))

def test_bad_boids_new_flock_vectorized():
    window_data = yaml.load(
        open(os.path.join(os.path.dirname(__file__), 'fixture.yml')))
    window_limits = np.array(window_data['window_limits'])
    count_limits = window_data['count_limits']
    boids_count = np.random.randint(count_limits[0], count_limits[1])
    vector_limits = window_data['vector_limits']
    vector_length = np.random.randint(vector_limits[0], vector_limits[1])
    lower_limits = np.random.uniform(window_limits[0], window_limits[1], vector_length)
    upper_limits = np.random.uniform(lower_limits, window_limits[1])
    points = new_flock(boids_count, lower_limits, upper_limits)
    print points
    print lower_limits
    print upper_limits
    in_range = np.logical_and(points >= lower_limits[:, np.newaxis], points <= upper_limits[:, np.newaxis])
    assert_true(np.all(in_range))
