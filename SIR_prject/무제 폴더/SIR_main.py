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
# setting the location for 100 people
population_number = 100
land_size = 100
infection_rate = 0.7
infection_distance = 2

population = range(population_number)
x_axis_location = []
y_axis_location = []
infection_status = [0 for i in range(population_number)]

infection_status[0] = 1  # setting patient zero




for nth_person in population:
    x_axis_location.append(random.randrange(1,land_size))
    y_axis_location.append(random.randrange(1,land_size))


fig = plt.figure()


def random_walk (axis,land_size):
    randomwalk = [-1,0,1]
    for nth_person in population:
        if axis[nth_person] == land_size:
            randomwalk = [-1,0]
        elif axis[nth_person] == 0:
            randomwalk = [0,1]
        axis[nth_person] = axis[nth_person] + random.choice(randomwalk)
        
    return axis


def animate(i):
    plt.clf()
    x_axis_location_new = random_walk(x_axis_location,land_size)
    y_axis_location_new = random_walk(y_axis_location,land_size)

    


    # for i in range(len(x_axis_location_new)):
    #      for j in range(i+1,len(x_axis_location_new+1)):
    #         abs(x_axis_location_new[i] - x_axis_location_new[j])        

    ax = plt.axes(xlim=(0,land_size+1), ylim=(0,land_size+1))

    dot = ax.plot(i,j,'r.')
    dot = ax.plot(x_axis_location_new[0],y_axis_location_new[0],'b.')
    return dot

anim = animation.FuncAnimation(
                                fig,
                                animate,
                                interval=500)

plt.show()
















