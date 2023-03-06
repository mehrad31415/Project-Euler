# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 11:29:20 2021

@author: Daneshjoei
"""
"""example 52:
    It can be seen that the number, 125874, and its double
    , 251748, contain exactly the same digits, but in a
    different order.

    Find the smallest positive integer, x, such that 2x,
    3x, 4x, 5x, and 6x, contain the same digits.
"""
counter=1
while True:
    if set(str(counter))==set(str(2*counter))==set(str(3*counter))==set(str(4*counter))==set(str(5*counter))==set(str(6*counter)):
        print (counter)
        break
    counter+=1
"""
#the running time of both codes is approx equal
counter=1
while True:
    if set(str(counter))==set(str(2*counter)):
        if set(str(2*counter))==set(str(3*counter)):
            if set(str(3*counter))==set(str(4*counter)):
                if set(str(4*counter))==set(str(5*counter)):
                    if set(str(5*counter))==set(str(6*counter)):
                        print (counter)
                        break
    counter+=1
"""    

