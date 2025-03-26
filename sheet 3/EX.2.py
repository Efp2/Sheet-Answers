# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 19:30:00 2025

@author: 𝐇𝐀𝐌𝐎𝐎𝐃
"""

fl_num = 1234.5678
bef_int_num = 2
aft_int_num = 3

num = str(fl_num)

integer_part, decimal_part = num.split('.')

X = integer_part[-bef_int_num:]

Y = decimal_part[:aft_int_num]

Z = float(f"{X}.{Y}")

print(Z)