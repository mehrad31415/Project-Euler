# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 17:38:52 2021

@author: Daneshjoei
"""
"""example 10:
    find the sum of all the primes below 2000000
"""
import math

#the function defines whether a number is a prime or not
def IsPrime(Num):
    for i in range (2,int(math.sqrt(Num))+1):
        if Num%i==0:
            return False
    return True


#in the above function if we write Num instead of
#int(Num**(1/2))+1 the calculation of the sum will take
#far longer. If we do no write the +1 then for instance
#6 will be recognized as a prime number by our function.

Sum=0
for i in range (2,2000000):
    if IsPrime(i):
        print(i)
        Sum+=i
print (Sum)        
