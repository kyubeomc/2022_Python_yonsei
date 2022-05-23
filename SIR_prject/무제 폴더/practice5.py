import os 
os.system('clear')

import numpy as np

A = [[[1,2,3,4,5,1,3,1],[2,3,4,5,5,6,3]],[[1,2,3,4],[1,2,3,4,5,6,1]]]

a = np.array(A)
index = np.where(a==1)
print(6 in A)

