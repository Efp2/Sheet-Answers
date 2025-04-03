# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 21:56:21 2025

@author: 𝐇𝐀𝐌𝐎𝐎𝐃
"""

import json

# 1. Create JSON file with users
users = [
    {"username": "Ahmed", "password": "A123#"},
    {"username": "Menna", "password": "M243*"},
    {"username": "Anas", "password": "A1A232"},
    {"username": "Omar", "password": "O01M32"}
]
My_file = open('users.json', 'w')
json.dump(users, My_file)
My_file.close()

# 2. Read and show first user
My_file = open('users.json', 'r')
users = json.load(My_file)
My_file.close()
print(f"First user: {users[0]['username']} , pass: {users[0]['password']}")

# 3. Add new user
users.append({"username": "Noor", "password": "N0O1#"})
My_file = open('users.json', 'w')
json.dump(users, My_file)
My_file.close()
print("User added")

# 4. Login check
u = input("Username: ")
p = input("Password: ")
My_file = open('users.json', 'r')
users = json.load(My_file)
My_file.close()

found = False
for user in users:
    if user['username'] == u and user['password'] == p:
        found = True
        break

print("Login Success!" if found else "Login Failed")