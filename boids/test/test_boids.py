from boids import Flock
from nose.tools import assert_almost_equal, assert_true
import os
import yaml
import numpy as np


def test_bad_boids_regression():
    regression_data = yaml.load(
        open(os.path.join(os.path.dirname(__file__), 'fixtures', 'update_fixture.yml')))
    boid_data = np.array(regression_data["before"])
    flock = Flock()
    flock.positions = boid_data[0]
    flock.velocities = boid_data[1]
    flock.update_boids()
    for after, before in zip(regression_data["after"], boid_data):
        for after_value, before_value in zip(after, before):
            assert_true(np.allclose(after_value, before_value, atol=0.01))

def test_bad_boids_new_flock_vectorized():
    window_data = yaml.load(
        open(os.path.join(
            os.path.dirname(__file__), 'fixtures', 'new_flock_fixture.yml')))
    window_limits = np.array(window_data['window_limits'])
    count_limits = window_data['count_limits']
    boids_count = np.random.randint(count_limits[0], count_limits[1])
    vector_limits = window_data['vector_limits']
    vector_length = np.random.randint(vector_limits[0], vector_limits[1])
    lower_limits = np.random.uniform(
        window_limits[0], window_limits[1], vector_length)
    upper_limits = np.random.uniform(
        lower_limits, window_limits[1])
    flock = Flock(
        boid_count=boids_count, position_limits=[lower_limits, upper_limits])
    in_range = np.logical_and(
        flock.positions >= lower_limits[:, np.newaxis],
        flock.positions <= upper_limits[:, np.newaxis])
    assert_true(np.all(in_range))

def test_flock_move():
    regression_data = yaml.load(
        open(os.path.join(
            os.path.dirname(__file__), 'fixtures', 'move_fixture.yml')))
    boid_data = np.array(regression_data["before"])
    flock = Flock()
    flock.positions = boid_data[0]
    flock.velocities = boid_data[1]
    flock.move()
    for after, before in zip(regression_data["after"], boid_data):
        for after_value, before_value in zip(after, before):
            assert_true(np.allclose(after_value, before_value, atol=0.01))

def test_flock_accelerate_to_middle():
    regression_data = yaml.load(
        open(os.path.join(
            os.path.dirname(__file__), 'fixtures', 'accelerate_to_middle_fixture.yml')))
    boid_data = np.array(regression_data["before"])
    flock = Flock()
    flock.positions = boid_data[0]
    flock.velocities = boid_data[1]
    flock.accelerate_to_middle()
    for after, before in zip(regression_data["after"], boid_data):
        for after_value, before_value in zip(after, before):
            assert_true(np.allclose(after_value, before_value, atol=0.01))

def test_flock_accelerate_from_boids():
    regression_data = yaml.load(
        open(os.path.join(
            os.path.dirname(__file__), 'fixtures', 'accelerate_from_boids_fixture.yml')))
    boid_data = np.array(regression_data["before"])
    flock = Flock()
    flock.positions = boid_data[0]
    flock.velocities = boid_data[1]
    flock.displacements_and_distances()
    flock.accelerate_from_boids()
    for after, before in zip(regression_data["after"], boid_data):
        for after_value, before_value in zip(after, before):
            assert_true(np.allclose(after_value, before_value, atol=0.01))

def test_flock_speed_match():
    regression_data = yaml.load(
        open(os.path.join(
            os.path.dirname(__file__), 'fixtures', 'speed_match_fixture.yml')))
    boid_data = np.array(regression_data["before"])
    flock = Flock()
    flock.positions = boid_data[0]
    flock.velocities = boid_data[1]
    flock.displacements_and_distances()
    flock.speed_match()
    for after, before in zip(regression_data["after"], boid_data):
        for after_value, before_value in zip(after, before):
            assert_true(np.allclose(after_value, before_value, atol=0.01))

def test_flock_displacements_and_distances():
    flock = Flock()
    flock.displacements_and_distances()
    transpose_positions = flock.positions.T
    for i, pos_i in enumerate(transpose_positions.tolist()):
        for j, pos_j in enumerate(transpose_positions.tolist()):
            displacement_check = np.array(pos_j) - np.array(pos_i)
            distance_check = np.sum(displacement_check**2)
            assert_true(np.all(flock.displacements[:, i, j] == displacement_check))
            assert_true(flock.square_distances[i, j] == distance_check)
