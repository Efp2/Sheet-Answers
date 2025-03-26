# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 10:44:48 2025

@author: 𝐇𝐀𝐌𝐎𝐎𝐃
"""

x=int(input("enter value of x "))
y=int(input("enter value of y "))

remainder =  y % x # TODO compute the remainder
quotient =  y // x # TODO compute the quotient

print("remainder is {} , and quotient is {}".format(remainder, quotient)) # TODO 1st way
print("remainder is {0} , and quotient is {1}".format(remainder, quotient))  # TODO 2nd way
print(f"remainder is {remainder} , and quotient is {quotient}")  # TODO 3rd way 