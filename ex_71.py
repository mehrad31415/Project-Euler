# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 12:55:36 2021

@author: Daneshjoei
"""
"""example 71:
    Consider the fraction, n/d, where n and d are
    positive integers. If n<d and HCF(n,d)=1, it is
    called a reduced proper fraction.

    If we list the set of reduced proper fractions for 
    d ≤ 8 in ascending order of size, we get:

    1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7,
    1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7,
    7/8

    It can be seen that 2/5 is the fraction immediately
    to the left of 3/7.

    By listing the set of reduced proper fractions for
    d ≤ 1,000,000 in ascending order of size, find the
    numerator of the fraction immediately to the left 
    of 3/7.
"""

#the function below defines whether Num1 and Num2
#are coprime or not
def coprime(Num1, Num2):
    assert Num1>Num2 and Num2>=1
    if Num2==1:
        return True
    while True:
        temp=Num1
        Num1=Num2
        Num2=temp%Num2
        if Num2==0:
            if Num1==1:
                return True
            return False
        
#test: print (coprime(10,3))
temp=2/5
for i in range (1,1000000):
    for j in range (((3*i)//7),1,-1):
        if temp>j/i:
            break
        if coprime(i,j):
            if 3/7>j/i:
                temp=j/i
                print (j)
                break

                
            
        
        
        