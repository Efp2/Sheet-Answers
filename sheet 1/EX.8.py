# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 10:45:12 2025

@author: 𝐇𝐀𝐌𝐎𝐎𝐃
"""

print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Enter a Choice (1, 2)): ")
choice = int(choice) - 1

temperature = input("Enter a temperature: ")
temperature = float(temperature)

converted = (temperature * 9 / 5 + 32) * (1 - choice) + ((temperature - 32) * 5 / 9) * choice

print(f"Result: {converted}") 