# SIR simulator COVID-19
# 2021.5.19
# Kyubeom Choi

import os 
os.system('clear')

import random
import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import itertools
import time
# setting the location for 100 people
population_number = 100
land_size = 30
infection_rate = 0.7
infection_distance = 2

population = range(population_number)
x_axis_location_healthy = []
y_axis_location_healthy = []
x_axis_location_infected = []
y_axis_location_infected = []
x_axis_location_cured = []
y_axis_location_cured = []




# setting the first coordinate for 100 people
for nth_person in range(population_number-1):
    x_axis_location_healthy.append(random.randrange(1,land_size))
    y_axis_location_healthy.append(random.randrange(1,land_size))

x_axis_location_infected.append(random.randrange(1,land_size))
y_axis_location_infected.append(random.randrange(1,land_size))






fig = plt.figure()
ax = fig.add_subplot(111)
line1, = ax.plot(x_axis_location_healthy, y_axis_location_healthy,"r.")
line2, = ax.plot(x_axis_location_infected, y_axis_location_infected,"b.")

def random_walk (axis,land_size):
    randomwalk = [-1,0,1]
    for nth_person in population:
        if axis[nth_person] == land_size:
            randomwalk = [-1,0]
        elif axis[nth_person] == 0:
            randomwalk = [0,1]
        axis[nth_person] = axis[nth_person] + random.choice(randomwalk)
        
    return axis






for iteration in range(20): 

    


    for (ix,iy) in zip(x_axis_location_infected,y_axis_location_infected):
        for (hx, hy) in zip(x_axis_location_healthy, y_axis_location_healthy):
            distance = ((ix - hx)**2 + (iy - hy)**2)**0.5
            if distance < 2:
                x_axis_location_infected.append(hx)
                y_axis_location_infected.append(hy)

                x_axis_location_healthy.remove(hx)
                y_axis_location_healthy.remove(hy)


    x_axis_location_healthy = random_walk(x_axis_location_healthy, land_size)
    y_axis_location_healthy = random_walk(y_axis_location_healthy, land_size)
    x_axis_location_infected = random_walk(x_axis_location_infected, land_size)
    y_axis_location_infected = random_walk(y_axis_location_infected, land_size)

    line1.set_xdata(x_axis_location_healthy)
    line1.set_ydata(y_axis_location_healthy)
    line2.set_xdata(x_axis_location_infected)
    line2.set_ydata(y_axis_location_infected)


    fig.canvas.draw()

    fig.canvas.flush_events()
    time.sleep(1)