# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 20:21:47 2021

@author: Daneshjoei
"""
"""example 16:
    What is the sum of the digits of the number 2^1000?
"""

#the function gives the number of digits of Num
def NumOfDigits(Num):
    counter=1
    while True:
        check=Num//(10**counter)
        if check==0:
            return counter
        counter+=1
#print(NumOfDigits(2**1000))=302

#the function gives us the sum of the digits of a number
def SumOfDig(Num):
    Sum=0
    Sum+=Num//(10**(NumOfDigits(Num)-1))
    Sum+=Num%10
    for i in range(1,NumOfDigits(Num)-1):
        Sum+=(Num//(10**i))%(10)
    return Sum
print(SumOfDig(2**1000))
    
    
        