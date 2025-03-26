# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 20:34:45 2025

@author: 𝐇𝐀𝐌𝐎𝐎𝐃
"""

d1 = {'a': 1}
d2 = {'a': 2}
d3 = {'b': 3}
all_dicts = [d1, d2, d3]

fin_di = {}

for D in all_dicts:
    fin_di.update(D)

print(fin_di)