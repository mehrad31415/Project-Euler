# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 17:55:56 2021

@author: Daneshjoei
"""
"""example 47:
    The first two consecutive numbers to have 
    two distinct prime factors are:

    14 = 2 × 7
    15 = 3 × 5

    The first three consecutive numbers to have 
    three distinct prime factors are:

    644 = 2² × 7 × 23
    645 = 3 × 5 × 43
    646 = 2 × 17 × 19.

    Find the first four consecutive integers to 
    have four distinct prime factors each. 
    What is the first of these numbers?
"""
import math
import time
#time the execution begins
begin=time.time()

#The function below gives the number of prime factors
def npf(Num):
    counter=0
    """why int(math.sqrt(Num))+1? because all the prime
    factors of Num are smaller than this number
    and at most Num has one prime factor bigger 
    than its square root. As if it should have
    2 prime factors the product of the numbers
    although being bigger than Num is a divisor 
    of Num and this is not possible!!!
    """
    for i in range (2,int(math.sqrt(Num))+1):
        if Num%i==0:
            counter+=1
        while Num%i==0:
            Num=Num//i 
            if Num==1:
                return counter
            #writing Num==1 here and not outsite the 
            #for-loop will make our algorithm more quicker
    return counter+1
    #incase the number has a prime factor bigger than
    #its square root. think about the algorithm
    
#test: print (npf(30))

#the following function returns true if the num of
#prime factors of Num are 4
#def IsFour(Num):
#    if NumOfPrimeFactors(Num)==4:
#        return True
#    else:
#        return False
"""defining the above function will only increase our
running time"""
Start=420#starting from 2^2*3*5*7
#why 420: because 210 is the lowest number containing
#4 distinctive prime factors and because one number 
#among 4 consecutive numbers is divisible it must be
#divisible by 2^2
while True:
    if npf(Start)==4:
        if npf(Start+1)==4:
            if npf(Start+2)==4:
                if npf(Start+3)==4:
                    print (Start)
                    break
    Start+=1
"""def call():
    j = 2*3*5*7
    while True:
        for i in range (4):
            if npf(j+i)!=4:
                break
        else:
            return j
        j += 1
print (call())
#writing the above instead of line 36-42 will only
increase your running time.
"""
#time the execution ends
end=time.time()
#total time of the execution
print(end-begin)