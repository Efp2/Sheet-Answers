# -*- coding: utf-8 -*-
"""
Created on Tue Mar 11 20:20:14 2025

@author: 𝐇𝐀𝐌𝐎𝐎𝐃
"""

USERS = {'user1': 'password1', 'user2': 'password2'}

name_input = input("Enter your username: ")
pass_input = input("Enter your password: ")

if name_input in USERS and USERS[name_input] == pass_input:
    print(f" Welcome Back , {name_input} ! ")
else:
    print("Wrong username or password!!")