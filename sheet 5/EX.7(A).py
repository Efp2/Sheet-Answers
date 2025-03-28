# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 23:27:22 2025

@author: 𝐇𝐀𝐌𝐎𝐎𝐃
"""


class Point2D:
    ##The constructor method, initializes a Point2D object with x and y coordinates
    def __init__(self, x=0, y=0):  
        self.x = x
        self.y = y
#self.x = x and self.y = y store the coordinates as instance attributes.
    def __str__(self):
        # the point is printed as a string 
        return f"({self.x}, {self.y})"

    def add(self, p):
        #Takes another Point2D (p) and adds its coordinates to the current point
        self.x += p.x
        self.y += p.y

    def distance(self, p):
        #Computes the Euclidean distance between self and another point p.
        delta_x = self.x - p.x
        delta_y = self.y - p.y

        dist = (delta_x ** 2 + delta_y ** 2) ** 0.5 #The Formula
        return dist


p1 = Point2D(1, 2) # Create point (1, 2)
p2 = Point2D(4, -2) ## Create point (4, -2)


p2.add(p1) # Add p1 to p2

print(p2) # Print The output
print(p1.distance(p2)) # The distance between p1 (1,2) and p2 (5,0)