# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 15:11:18 2021

@author: Daneshjoei
"""
"""example9:
    There exists exactly one Pythagorean triplet
    for which a + b + c = 1000.
    Find the product abc.
"""
#range 333-1000 because c is the largest
def pythagorean():
    for c in range (333,1000):
        for a in range (1,c):
            b=1000-c-a
            if b**2+a**2==c**2:
                return a*b*c, (a,b,c)
            
print (pythagorean())