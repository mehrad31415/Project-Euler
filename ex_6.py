# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 14:25:03 2021

@author: Daneshjoei
"""
"""example6:
    find the difference between the sum of the squared 
    first one hundred natural numbers and the square of the
    sum of the first one hundred natural numbers!
"""
Sum1=Sum2=0
for i in range (1,101):
    Sum1+=i**2
    Sum2+=i
print (abs(Sum1-(Sum2**2)))