# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 21:45:46 2025

@author: 𝐇𝐀𝐌𝐎𝐎𝐃
"""

My_file = open("Sheet 6.txt", "a")
for S in range(1, 101):
    My_file.write(f"{S}\n")
My_file.close()