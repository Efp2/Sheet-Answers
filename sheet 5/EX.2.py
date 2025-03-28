# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 21:50:10 2025

@author: 𝐇𝐀𝐌𝐎𝐎𝐃
"""


x_coor = [1, 2, 3, 4, 5]
y_coor = [2, 4, 6, 8, 10]
z_coor = [0, -1, -2, -3, -4]

points = [(x, y, z) for x, y, z in zip(x_coor, y_coor, z_coor)]
"""
Takes one item from each input iterable at the same index.

Pairs them into a tuple.
"""

print(points)