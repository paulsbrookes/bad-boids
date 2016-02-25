Bad Boids

Bad boids is a package which allows you to simulate the motion of birds using
the boids model in which birds are represented by points in a 2D plane which
attract each other, match speed within a certain distance and repel each other
if they become too close. A collection of boids is represented using the
boids.Flock class.

Flock takes the following kwargs:
position_limits - the window within which initial boid positions are generated.
velocity_limits - the window within which initial boid velocities are generated.
boid_count - the number of boids in the flock.
attraction_strength - the strength with which boids attract each other.
repulsion_distance - the distance within which boids beginning repelling.
speed_match_strength - the rate at which boids match speeds.
speed_match_distance - the distance within which boids begin matching speeds.

Flock has the following methods:
accelerate_to_middle - adjust velocites according attraction between boids.
displacements_and_distances - calculate distances and displacements between
boids.
accelerate_from_boids - adjust velocities according to repulsion between boids
which are too close.
speed_match - adjust velocities so that nearby boids match speeds.
move - move the boids according to their velocities.
update_boids - carry out an iteration of boid velocity adjustmente and movement.
animate - animate the boids.

This pakcage includes a command line interface.

usage: animation.py [-h] [--def_params DEF_PARAMS] [--boid_count BOID_COUNT]
                    [--attraction_strength ATTRACTION_STRENGTH]
                    [--repulsion_distance REPULSION_DISTANCE]
                    [--speed_match_strength SPEED_MATCH_STRENGTH]
                    [--speed_match_distance SPEED_MATCH_DISTANCE]

Boid simulation:simulates the movement of birds using the Boid model.

optional arguments:
  -h, --help            show this help message and exit
  --def_params DEF_PARAMS, -c DEF_PARAMS
                        File containing default parameters for the boids
                        simulation.
  --boid_count BOID_COUNT
                        Specify the number of boids.
  --attraction_strength ATTRACTION_STRENGTH
                        Specify the attraction strength between the boids.
  --repulsion_distance REPULSION_DISTANCE
                        Specify the distance below which boids repel each
                        other.
  --speed_match_strength SPEED_MATCH_STRENGTH
                        Specify the rate at which boids match their speeds.
  --speed_match_distance SPEED_MATCH_DISTANCE
                        Specify the distance below which boids begin #
                        matching their speeds.
