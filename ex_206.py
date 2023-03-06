# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 19:38:44 2021

@author: Daneshjoei
"""
"""example 206:
    Find the unique positive integer whose square has the 
    form 1_2_3_4_5_6_7_8_9_0,
    where each “_” is a single digit.
"""
#because this number ends with a zero it has divisors
#2 and 5 and being a square number it has to have atleast
#have another divisor of 2 and 5; So the number is like:
#1_2_3_4_5_6_7_8_900 we have to find :
#1_2_3_4_5_6_7_8_9 which is a squared number.(17-digited)
#10^8 squared is the smallest 17-digited number
import math
N=int(math.sqrt(10**17)) 
#N is the largest number when squared is 17 digited

def Check(Num):
    #Num is 17 digited
    nine=Num%10
    one=Num//(10**16)
    if one !=1 or nine!=9:
        return False
    for i in range(2,16,2):
        check=Num%(10**(i+1))//10**i  
        if check !=9-(i//2) :
            return False
    return True

for i in range (10**8, N+1):
    Num=i**2
    if Check(Num):
        print (math.sqrt(Num)*10)
        break
    
    
    
    
    
