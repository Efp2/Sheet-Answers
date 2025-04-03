# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 21:49:11 2025

@author: 𝐇𝐀𝐌𝐎𝐎𝐃
"""

My_file = open("Sheet 6.txt", "r")
y = My_file.readlines()  
My_file.close()

for x in y[49:60]:  
    print(x.strip())  