# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 12:45:03 2021

@author: Daneshjoei
"""
"""example 25:
    The Fibonacci sequence is defined by the 
    recurrence relation:

    Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
    Hence the first 12 terms will be:
    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144
    The 12th term, F12, is the first term to contain 
    three digits.
    What is the index of the first term in the 
    Fibonacci sequence to contain 1000 digits?
"""
#the function gives the Num'th fibonacci number
#below is recursive
#def fibonacci(Num):
#    if Num==1 or Num==2:
#        return 1
#    else:
#        return fibonacci(Num-1)+fibonacci(Num-2)
def fibonacci(Num):
    first=0
    second=1
    for i in range (Num):
        temporary=first
        first=second
        second=temporary+second
    return first         
#test: print (fibonacci(12))

#the function gives the number of digits
def NumOfDigits(Num):
    counter=1
    while True:
        temporary=Num//(10**counter)
        if temporary==0:
            return counter
        counter+=1
#test: print (NumOfDigits(1111))
Num=1
while True:
    if NumOfDigits(fibonacci(Num))==1000:
        print (Num)
        break 
    Num+=1           
    
    



    