# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 22:44:53 2021

@author: Daneshjoei
"""
"""example 40:
    An irrational decimal fraction is created 
    by concatenating the positive integers:

    0.123456789101112131415161718192021...

    It can be seen that the 12th digit of the
    fractional part is 1.

    If dn represents the nth digit of the fractional 
    part, find the value of the following expression.

    d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""
#the function below calculates the num of digits
#of the number by concatenating all 1 to "n" digit-numbers
def NumOfDigits(n):
    s=0
    for i in range (1,n+1):
        s+=(9*(10**(i-1)))*i
    return s
#the function below gives the biggest "n" digit number
def biggestNumber(n):
    return (10**n)-1
#it is obvious that the first digit is 1
temp=1
total=1
for i in range (1,7):
    #defining temp will speed your algorithm (why?)
    n=temp
    while True:
        if NumOfDigits(n)>10**i:
            temp=n
            #print (n)
            break
        n+=1
    #Num is the number which contains "d10..."
    Num=biggestNumber(n-1)+(((10**i)-NumOfDigits(n-1))//n)+1
    #which digit of Num should be counted? answer below
    total*=(Num//(10**(n-(((10**i)-NumOfDigits(n-1))%n))))%(10)
print (total)    
    
    
