#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

g = 9.81

# intial lengths and masses of both pendulums
L1 = 1.0
L2 = 1.0
m1 = 1.0
m2 = 1.0

def double_pendulum(tmax, dt, init_conditions):
    # initialize starting angles and velocities
    theta1, theta2, omega1, omega2 = init_conditions

    # initial time, maximum duration, and the time step
    t0 = 0.0
    tmax = tmax
    dt = dt
    # calculate the number of time steps
    num_steps = int((tmax - t0) / dt)

    def derivs(state, t):
        """
        Calculates the derivatives of the state variables

        param: state is the current state of the double pendulum including starting angles and velocities
               of both pendulums
        param: t is an array time steps from the starting time to the stop time

        """

        theta1, theta2, omega1, omega2 = state
        
        # derivative of angular pos = angular vel
        dtheta1dt = omega1
        dtheta2dt = omega2

        sin_delta_theta = np.sin(theta1 - theta2)
        cos_delta_theta = np.cos(theta1 - theta2)
        
        # calculate the derivatives of the angular velocities (angular acceleration)
        domega1dt = (m2 * g * np.sin(theta2) * cos_delta_theta - m2 * sin_delta_theta * (L1 * omega1 ** 2 * cos_delta_theta + L2 * omega2 ** 2) - (m1 + m2) * g * np.sin(theta1)) / (L1 * (m1 + m2 * sin_delta_theta ** 2))
        domega2dt = ((m1 + m2) * (L1 * omega1 ** 2 * sin_delta_theta - g * np.sin(theta2) + g * np.sin(theta1) * cos_delta_theta) + m2 * L2 * omega2 ** 2 * sin_delta_theta * cos_delta_theta) / (L2 * (m1 + m2 * sin_delta_theta ** 2))
        # return derivatives
        return [dtheta1dt, dtheta2dt, domega1dt, domega2dt]

    state0 = [theta1, theta2, omega1, omega2]

    t = np.linspace(t0, tmax, num_steps)
    # solve the ODE's for the double pendulum system
    y = odeint(derivs, state0, t)
    
    return t, y

t, y = double_pendulum(20, 0.01, [np.pi/2, np.pi/2, 0, 0])

# calculate the x and y positions of both pendulums using trigonometric functions
x1 = L1 * np.sin(y[:, 0])
y1 = -L1 * np.cos(y[:, 0])
x2 = x1 + L2 * np.sin(y[:, 1])
y2 = y1 - L2 * np.cos(y[:, 1])

plt.plot(x1, y1, 'b', label='Pendulum 1')
plt.plot(x2, y2, 'g', label='Pendulum 2')
plt.title('Double Pendulum Simulation')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.legend()
plt.show()

