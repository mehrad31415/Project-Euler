# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 23:58:50 2021

@author: Daneshjoei
"""
"""example 24:
    What is the millionth lexicographic permutation of 
    the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""

from itertools import permutations
counter=0
for i in permutations(list(range(10))):
    counter+=1
    if counter==1000000:
        print (i)
        break