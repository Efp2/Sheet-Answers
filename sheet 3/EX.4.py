# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 20:04:02 2025

@author: 𝐇𝐀𝐌𝐎𝐎𝐃
"""

sequence = [10, 20, 30, 40, 50, 60]

even_sum = 0
odd_sum = 0
i = 0

while i < len(sequence):
    if i % 2 == 0:  
        even_sum += sequence[i]
    else:  
        odd_sum += sequence[i]
    i += 1

print(f" The of evens is: {even_sum} , and the sum of odds is: {odd_sum} .")