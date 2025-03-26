# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 20:35:57 2025

@author: 𝐇𝐀𝐌𝐎𝐎𝐃
"""

numbers1 = [10, 20, 30]
numbers2 = [10, 20, 30, 10, 40,  20, 30, 20, 30 , 10] #[10, 20, 30, 40]

unique_X = len(set(numbers1))
unique_Y = len(set(numbers2))

print(f"Unique numbers in numbers1: {unique_X} , Unique numbers in numbers2: {unique_Y}")
