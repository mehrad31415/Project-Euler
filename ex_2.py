# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 09:54:37 2021

@author: Daneshjoei
"""

"""example2:
      find the sum of the even fibonacci numbers below
      4 million.
"""

def SumEvenFib():
    First=1
    Second=2
    Sum=0
    while First<4000000:
        Third=First+Second#3,5
        First=Second#2,3
        Second=Third#3,5
        if First%2==0:
            Sum+=First
    return Sum
print(SumEvenFib())
    
"""Method 2: much less efficient!
#fib(Num) is the "Num" fibonacci number
def fib(Num):
    if Num==1:
        return 1
    elif Num==2:
        return 2
    else:
        return fib(Num-1)+fib(Num-2)  
Sum=0
counter=1
while fib(counter)<4000000:
    if fib(counter)%2==0:
        Sum+=fib(counter)
    counter+=1
print (Sum)        
"""
        
        