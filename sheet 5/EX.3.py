# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 21:54:23 2025

@author: 𝐇𝐀𝐌𝐎𝐎𝐃
"""


"""

def apply(lst, fn):
    result = []
    for elem in lst:
        result.append(fn(elem))
    return result

def add_1(num):
    return num + 1

r = apply([1, 2, 3], add_1)
print(r) ### output ==> [2, 3, 4]

"""

def plus_1(x):
    return x + 1

r = list(map(plus_1, [1, 2, 3]))  
print(r)  