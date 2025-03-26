# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 05:56:54 2025

@author: 𝐇𝐀𝐌𝐎𝐎𝐃
"""

def substitute(equation, **kwargs):
    for X, Y in kwargs.items():
        equation = equation.replace(X, str(Y))
    return equation

The_equation =substitute("x + 4 - y + 3 * z", x=7, y=8, z=6)
print(The_equation)