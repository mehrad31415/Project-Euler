# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 17:40:48 2021

@author: Daneshjoei
"""
"""example 48:
    The series 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317

    Find the last ten digits of the series,
    1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""
#The function gives the number of digits of Num:
def NumOfDigits(Num):
    counter=1
    while True:
        if Num//(10**counter)==0:
            return counter
        counter+=1        
#test: print (NumOfDigits(3434231298))

#The function gives the last i digits of Num
def TheLastDigits(Num,i):
    if i>NumOfDigits(Num):
        return "your number is {}-digited".format(NumOfDigits(Num))
    return Num%(10**i)
#test: print(TheLastDigits(85621,5))
Sum=0
for i in range (1,1001):
    Sum+=(i**i)
print (TheLastDigits(Sum,10))
    