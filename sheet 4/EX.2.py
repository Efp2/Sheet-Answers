# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 04:47:50 2025

@author: 𝐇𝐀𝐌𝐎𝐎𝐃
"""
all_chars = ''.join([chr(x) for x in range(97, 123)] +  # a-z
                    [chr(x) for x in range(65, 91)] +  # A-Z
                    [chr(x) for x in range(48, 58)])    # 0-9

print(all_chars)

for char in all_chars:
    print(f"{char}: {ord(char)}")