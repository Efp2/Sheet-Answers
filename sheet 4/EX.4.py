# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 05:25:29 2025

@author: 𝐇𝐀𝐌𝐎𝐎𝐃
"""

def average(*numbers):
    if not numbers:
        return 0
    sum_of_num = sum(numbers)
    
    count_of_num = len(numbers)
    
    return sum_of_num / count_of_num

z=average(30, 45, 17, 23, 104)
print(z)
