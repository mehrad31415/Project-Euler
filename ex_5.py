# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 10:54:00 2021

@author: Daneshjoei
"""
"""example5: 
    find the smallest multiple of numbers from 1-20
"""

#the function is calculating the GCD of two numbers
def gcd(Num1,Num2):
    if Num1==0: 
        if Num2==0:
            return 'No gcd'
        else:
            return Num2
    else:
        return gcd(Num2%Num1,Num1)
#LCM is the smallest multiple
LCM=1  
for i in range (2,21):
    LCM*=i/gcd(i,LCM)
print (LCM)
    
    
