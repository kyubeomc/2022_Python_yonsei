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

infection_status[0] = -1  # setting patient zero -1 is infected , -2 is healthy 




status = []
# setting patient // patient:-2, healthy:-1, cured:-3
#
#######################################################
# Variable Status = 

for nth_person in population:
    if nth_person == 0:
        status.append([[-2]])
    else:
        status.append([[-1]])

# setting the first position of the population
for nth_person in population:
    x_axis = random.randrange(1,land_size)
    y_axis = random.randrange(1,land_size)
    status[nth_person][0].append(x_axis)
    status[nth_person][0].append(y_axis)


for nth_person in population:
    for iteration in range(10):
        
        
        




    

print(status)



# for nth_person in population:
#     if nth_person == 0:
#         status[nth_person] = [[1,x_axis_location[nth_person],y_axis_location[nth_person]]]   
#     else :
#         status[nth_person] = [[0,x_axis_location[nth_person],y_axis_location[nth_person]]]

def random_walk (axis,land_size):
    randomwalk = [-1,0,1]
    if axis == land_size:
        randomwalk = [-1,0]
    elif axis == 0:
        randomwalk = [0,1]
    axis = axis + random.choice(randomwalk)
        
    return axis


# for iteration in range(20):
#     for nth_person in population:
#         x_axis = random_walk(status[nth_person][iteration][1],land_size)
#         y_axis = random_walk(status[nth_person][iteration][2],land_size)
#         status[nth_person].append([0,x_axis,y_axis])

    























# population = range(population_number)
# x_axis_location = []
# y_axis_location = []
# infection_status = [0 for i in range(population_number)]

# infection_status[0] = 1  # setting patient zero




# for nth_person in population:
#     x_axis_location.append(random.randrange(1,land_size))
#     y_axis_location.append(random.randrange(1,land_size))


# fig = plt.figure()


# def random_walk (axis,land_size):
#     randomwalk = [-1,0,1]
#     for nth_person in population:
#         if axis[nth_person] == land_size:
#             randomwalk = [-1,0]
#         elif axis[nth_person] == 0:
#             randomwalk = [0,1]
#         axis[nth_person] = axis[nth_person] + random.choice(randomwalk)
        
#     return axis


# def animate(i):
#     plt.clf()
#     x_axis_location_new = random_walk(x_axis_location,land_size)
#     y_axis_location_new = random_walk(y_axis_location,land_size)

    
#     t = t

#     # for i in range(len(x_axis_location_new)):
#     #      for j in range(i+1,len(x_axis_location_new+1)):
#     #         abs(x_axis_location_new[i] - x_axis_location_new[j])        

#     ax = plt.axes(xlim=(0,land_size+1), ylim=(0,land_size+1))
#     k = 0

#     for (i,j) in (zip(x_axis_location_new,y_axis_location_new)):
#         k = k+1
#         for (x,y) in zip(x_axis_location_new[k:],y_axis_location_new[k:]):
#             distance = (abs(i-x)**2 + abs(j-y)**2)**0.5 

        

#         dot = ax.plot(i,j,'r.')
#         dot = ax.plot(x_axis_location_new[0],y_axis_location_new[0],'b.')
#     return dot
# t= 1 
# anim = animation.FuncAnimation(
#                                 fig,
#                                 animate,
#                                 interval=500)

# plt.show()
















