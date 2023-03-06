# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 13:04:15 2021

@author: Daneshjoei
"""
"""example 21:
    Let d(n) be defined as the sum of proper divisors 
    of n (numbers less than n which divide evenly into n).
    If d(a) = b and d(b) = a, where a ≠ b, then a and b 
    are an amicable pair and each of a and b are called 
    amicable numbers.

    For example, the proper divisors of 220 are
    1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
    therefore d(220) = 284. The proper divisors of 284 
    are 1, 2, 4, 71 and 142; so d(284) = 220.

    Evaluate the sum of all the amicable numbers under
    10000.
"""

#this function gives the sum of the divisors of Num
def SumOfDivisors(Num):
    #numbers bigger than (Num//2)+1 none of them 
    #except for Num are a divisor of Num
    Sum=0
    for i in range (1,(Num//2)+1):
        if Num%i==0:
            Sum+=i
    return Sum
Summary=0
for i in range(1,10000):
    PossibleAmicable=SumOfDivisors(i)
    if i==SumOfDivisors(PossibleAmicable) and i!=PossibleAmicable:
        Summary+=i
#the question is when we search that i and 
#PossibleAmicable are amicables or not is it not
#better to not consider the PossibleAmicable again in the
#range to increase the speed of our algorithm???
#well if its only for the true amicable ones it will
#not increase the speed of our algorithm that much
#because the number of amicable numbers is low
#for non-amicable numbers because they consist a high
#majority of the numbers it will increase the speed
#of our algorithm but it will not be correct to do so
#take 1184,1490,1604,1898 all of which have a sum of
#divisors of 1210 but only 1184 is amicable with it
#if we were to delete 1210 when not being amicable with
#1490 for instance we could not check it with 1184.
#(here 1184 is checked first and we do not encounter
#such a problem but you get what I say hopefully)
print (Summary)