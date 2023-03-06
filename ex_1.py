# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 09:44:13 2021

@author: Daneshjoei
"""

"""example 1:
    find the sum of all multiples of 3 and 5 below 1000
"""
Sum=0
for i in range(1000):
    if i%3==0 or i%5==0:
        Sum+=i

print (Sum)