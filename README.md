# PHYS-5070-Final-Project

The goal of this project was to research the double pendulum and figure out how to calculate it's path; research equations used to do so and try to understand them to the best of my ability; and, once this has been done, create a python program that simulates a double pendulum that can change based on user defined starting conditions. I eventually had to settle for creating a plot of the motion of the pendulum without the visualization of it moving in real time due to time constriants though. 

The gravitational acceleration of the world, length of each pendulum, and masses of each pendulum are globally defined variables which the user can change at will. The initial position and angular velocities are also determined by the user but are set in the function call to 'double_pendulum'. 

Once the program is up and running, it program derives the angular velocity and acceleration of each pendulum. It then uses the 'odeint' function from scipy's integrate library in order to soolve the ODE's of the system. The solutions that this function provides are then used find the x and y positions of each pendulum over time through the use of trigonometry. The results are then plotted on an xy plot for the user to observe.

The included test suite is fairly self-explanatory through the comments posted throughout the code.
