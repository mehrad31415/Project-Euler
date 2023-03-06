# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 00:57:25 2021

@author: Daneshjoei
"""
"""example 92:
    A number chain is created by continuously 
    adding the square of the digits in a number
    to form a new number until it has been seen before.

    For example,

    44 → 32 → 13 → 10 → 1 → 1
    85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

    Therefore any chain that arrives at 1 or 89 will
    become stuck in an endless loop. What is most 
    amazing is that EVERY starting number will 
    eventually arrive at 1 or 89.

    How many starting numbers below ten million will 
    arrive at 89?
"""
#function gives the above process for one number
def SumOfSquareDigits(Num):
    while True:
        Sum=0
        Num_str=str(Num)
        for i in Num_str:
            Sum+=int(i)**2
        if Sum==89:
            return True
        if Sum==1:
            return False
        Num=Sum

#test: print (s(44))

counter=0          
for i in range(2,10000000):
    if SumOfSquareDigits(i):
        counter+=1
print (counter)
    