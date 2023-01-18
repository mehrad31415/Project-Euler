# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 21:39:15 2021

@author: Daneshjoei
"""
"""example 15:
    Starting in the top left corner of a 2×2 grid,
    and only being able to move to the right and down,
    there are exactly 6 routes to the bottom right corner.
    How many such routes are there through a 20×20 grid?
"""
#we want to creat a string of length 40 with "R" and "D"
#20 of each how many strings can we create?
#computes the number of non-repetitive permutations
"""
recursive programming:
def c(i,j):
    if i==j or j==0:
        return 1
    elif i<j:
        return 0
    else:
        return c(i-1,j-1)+c(i-1,j)
"""
#given n calculates n!
def factoriel(Num):
    Multi=1
    for i in range (1,Num+1):
        Multi*=i
    return Multi
#calculates the number of non-repetitive permutations
def c(i,j):
    return factoriel(i)/(factoriel(j)*factoriel(i-j))
print (c(40,20))
