#!/usr/bin/env python
# coding: utf-8


import numpy as np
from double_pendulum import double_pendulum

# Test 1: Test the output shape of the double pendulum function
t, y = double_pendulum(10, 0.01, [np.pi/2, np.pi/2, 0, 0])
assert y.shape == (1000, 4)

# Test 2: Test that the maximum value of t remains intact
assert t[-1] == 10

# Test 3: Test the initial position and velocities of the pendulums
t, y = double_pendulum(10, 0.01, [np.pi/2, np.pi/2, 0, 0])
assert np.allclose(y[0], [np.pi/2, np.pi/2, 0, 0])

# Test 4: Test the chaotic nature of the system by comparing the final positions of the pendulums for slightly different initial conditions
t, y1 = double_pendulum(10, 0.01, [np.pi/2, np.pi/2, 0, 0])
t, y2 = double_pendulum(10, 0.01, [np.pi/2+0.01, np.pi/2+0.01, 0, 0])
assert not np.allclose(y1[-1], y2[-1], atol=1e-1)

