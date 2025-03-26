# -*- coding: utf-8 -*-
"""
Created on Thu Mar  6 03:06:24 2025

@author: 𝐇𝐀𝐌𝐎𝐎𝐃
"""

my_str = "    hello           world          "

my_str = my_str.strip() #"hello world"
my_str = my_str.title() #"Hello World"
sub_strs = my_str.split(' ') #['Hello', '', '', '', '', '', '', '', '', 'World']
my_str = sub_strs[0].upper() + ', ' + "python".title() + '!' #"HELLO, Python!"
print(my_str)