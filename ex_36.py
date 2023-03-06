# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 15:02:07 2021

@author: Daneshjoei
"""
"""example 36: 
    The decimal number, 585 = 10010010012 (binary),
    is palindromic in both bases.

    Find the sum of all numbers, less than one million,
    which are palindromic in base 10 and base 2.

    (Please note that the palindromic number, 
     in either base, may not include leading zeros.)
"""
#the function defines whether a number is palindrome
def IsPalindrome(Num):
    Num_str=str(Num)
    for i in range (0,len(Num_str)//2):
        if Num_str[i]!=Num_str[len(Num_str)-i-1]:
            return False
    return True

#Test: print (IsPalindrome(58585))

#the function returns the base two of a number
def BaseTwo(Num):
    counter=0
    Sum=0
    while True:
        remainder=Num%2
        Sum+=remainder*(10**counter)
        Num=Num//2
        if Num==1:
            Sum+=Num*(10**(counter+1))
            return Sum
        counter+=1
#test: print (BaseTwo(11))


S=0
#one-digit numbers are all palindromes 
#only need need to be ckecked for their base two
#and we cannot use the ispalindrome function for 
#defining whether a one digit number is palindrome or not
#because of the range
for i in range (2,10):
    if IsPalindrome(BaseTwo(i)):
        S+=i
for i in range (10,1000000):
    if IsPalindrome(i):
        if IsPalindrome(BaseTwo(i)):
            S+=i
#the plus one is for 1 which is one digited in 
#base 10 and base 2
print (S+1)




