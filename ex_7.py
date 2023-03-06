# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 14:36:51 2021

@author: Daneshjoei
"""
"""example 7:
    find the 10,001'th prime number
"""
#the function finds if a number is prime or not
def IsPrime(Num):
    for i in range(2,Num):
        if Num%i==0:
            return False
    return True
#counter is for counting the number of prime numbers
counter=0
Num=2
while True:
    if IsPrime(Num):
        counter+=1
        if counter==10001:
            print (Num)
            break
    Num+=1
