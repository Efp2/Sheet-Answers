# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 15:40:06 2025

@author: 𝐇𝐀𝐌𝐎𝐎𝐃
"""

import numpy as np

a = np.arange(100).reshape(-1, 10)  
# 9:
b = a[9][2]
print(b)

print("\n-------------------------------------------------------------------------\n")

# 10:
row3 = a[2, :]
print(row3)

print("\n-------------------------------------------------------------------------\n")

# 11:
column4 = a[:, 3]
print(column4)