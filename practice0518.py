# SIR simulator COVID-19
# 2021.5.19
# Kyubeom Choi

import os 
os.system('clear')

import random
import matplotlib.pyplot as plt
# setting the location for 100 people
population_number = 100
land_size = 30

population = range(population_number)
x_axis_location = []
y_axis_location = []
investion_status = [0 for i in range(population_number)]

investion_status[0] = 1  # setting patient zero

for nth_person in population:
    x_axis_location.append(random.randrange(1,land_size+1))
    y_axis_location.append(random.randrange(1,land_size+1))






# applying random walk for each indiviual

randomwalk = [-1,0,1]
for nth_person in population:
    x_axis_location[nth_person] = x_axis_location[nth_person] + random.choice(randomwalk)

for nth_person in population:
    y_axis_location[nth_person] = y_axis_location[nth_person] + random.choice(randomwalk)

plt.plot(x_axis_location,y_axis_location)
plt.show()
    
    









