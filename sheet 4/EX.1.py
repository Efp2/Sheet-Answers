# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 04:31:37 2025

@author: 𝐇𝐀𝐌𝐎𝐎𝐃
"""

import random

def generate_password(length, chars):
    password = ''.join(random.choices(chars, k=length))
    return password

print(generate_password(8, "abcde"))