# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 15:29:18 2025

@author: 𝐇𝐀𝐌𝐎𝐎𝐃
"""

import numpy as np
# 6:
array_2d = np.arange(1, 10).reshape(3, 3)
print(array_2d)

print("\n-------------------------------------------------------------------------\n")

# 7:
array_1d = array_2d.flatten()  
print(array_1d)

print("\n-------------------------------------------------------------------------\n")

# 8:
my_array = np.arange(100)  
new_array = my_array.reshape(4, -1)  
print(new_array)

print('the shape is: ',  new_array.shape)