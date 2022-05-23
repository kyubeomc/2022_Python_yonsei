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




# random walk function 
def random_walk (axis,land):
    randomwalk = [-1,0,1]
    for nth_person in range(len(axis)):
        
        # if the person is standing on the edge control the random variable to get it inside
        if axis[nth_person] == land:
            randomwalk = [-1,0]
        elif axis[nth_person] == 0:
            randomwalk = [0,1]
        axis[nth_person] = axis[nth_person] + random.choice(randomwalk)
        
    return axis



# settings 
##########################   CHANGE THIS    ##############################

population_number = 1000
land_size = 250
infection_rate = 0.9
infection_distance = 2
cure_rate = 0.002

##########################################################################



population = range(population_number)
x_axis_location_healthy = []
y_axis_location_healthy = []
x_axis_location_infected = []
y_axis_location_infected = []
x_axis_location_cured = []
y_axis_location_cured = []
cured = []
infected = []
healthy = []



# setting the first coordinate 
for nth_person in range(population_number):
    x_axis_location_healthy.append(random.randrange(1,land_size))
    y_axis_location_healthy.append(random.randrange(1,land_size))

x_axis_location_infected.append(random.randrange(1,land_size))
y_axis_location_infected.append(random.randrange(1,land_size))



# making the figure real time plotting
plt.ion() 
fig = plt.figure(figsize=(6,12))


for p in range(2000):
    plt.pause(0.015) # pausing at each cicle
    plt.clf()
    for (ix,iy) in zip(x_axis_location_infected,y_axis_location_infected): # infected x/y coordinate
        for (hx, hy) in zip(x_axis_location_healthy, y_axis_location_healthy): # healthy x/y coordinate

            #if the distance is lower then 2 make it infected
            distance = ((ix - hx)**2 + (iy - hy)**2)**0.5
            
            if distance < 2 and infection_rate > random.random():
                x_axis_location_infected.append(hx)
                y_axis_location_infected.append(hy)

                x_axis_location_healthy.remove(hx)
                y_axis_location_healthy.remove(hy)

    # just to make sure the population is all infected // (optional)
    if len(x_axis_location_infected) > 20:
        for (ix,iy) in zip(x_axis_location_infected,y_axis_location_infected):
            if cure_rate > random.random():
                x_axis_location_cured.append(ix)
                y_axis_location_cured.append(iy)   
                
                x_axis_location_infected.remove(ix)
                y_axis_location_infected.remove(iy)      

    # random walk for all healthy & infected & cured
    x_axis_location_healthy = random_walk(x_axis_location_healthy, land_size)
    y_axis_location_healthy = random_walk(y_axis_location_healthy, land_size)
    x_axis_location_infected = random_walk(x_axis_location_infected, land_size)
    y_axis_location_infected = random_walk(y_axis_location_infected, land_size)
    x_axis_location_cured = random_walk(x_axis_location_cured, land_size)
    y_axis_location_cured = random_walk(y_axis_location_cured, land_size)
    
    
    cured.append(len(x_axis_location_cured))
    healthy.append(len(x_axis_location_healthy))
    infected.append(len(x_axis_location_infected))
    plt.subplot(2,1,1)
    
    # simulation plot
    plt.plot(x_axis_location_healthy, y_axis_location_healthy,"b.")
    plt.plot(x_axis_location_infected, y_axis_location_infected,"r.")
    plt.plot(x_axis_location_cured, y_axis_location_cured, 'g.')
    plt.xlim(0,land_size)
    plt.ylim(0,land_size)
    plt.title('SIR Simulator')

    #plotting the graph
    plt.subplot(2,1,2)

    plt.plot(range(len(cured)),cured,'g')
    plt.plot(range(len(cured)),healthy,'b')
    plt.plot(range(len(cured)),infected,'r')
    plt.xlabel('time / d')
    plt.ylabel('number')
    plt.title('SIR Graph')


    plt.show()

    #checking the numbers
    print(len(x_axis_location_healthy))
    print(len(x_axis_location_cured))
    print(len(x_axis_location_infected))

    if len(x_axis_location_cured) > population_number-20:
        break


    




                

