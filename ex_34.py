# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 22:34:35 2021

@author: Daneshjoei
"""

"""example 34:
    145 is a curious number, as 
    1! + 4! + 5! = 1 + 24 + 120 = 145.

    Find the sum of all numbers which are equal to the
    sum of the factorial of their digits.

    Note: As 1! = 1 and 2! = 2 are not sums they are
    not included.
"""

def factoriel(Num):
    product=1
    for i in range (2,Num+1):
        product*=i
    return product
#test: print (factoriel(4))

def Digit(Num):
    str_Num=str(Num)
    Sum=0
    for i in str_Num:
        Sum+=factoriel(int(i))
    return Sum
#test: print (Digit(145))
#now how to define an upper bound???
""" bigger than 999,999 will not do
print (Digit(9999999))
"""
S=0
for i in range (3,999999):
    if Digit(i)==i:
        S+=i
print (S)
        
        