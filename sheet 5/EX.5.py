# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 23:20:24 2025

@author: 𝐇𝐀𝐌𝐎𝐎𝐃
"""

def modlist(lst):
    for i in range(len(lst)):
        lst[i] = 10 * lst[i]

def modvar(num):
    num += 10

lst = [1, 2, 3]
modlist(lst)
print(lst)

x = 0
modvar(x) # Output from `print(lst)`
print(x)  # Output from `print(x)`