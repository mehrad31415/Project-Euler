# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 10:22:17 2021

@author: Daneshjoei
"""
"""example4:
    find the largest palindrome number which is a product
    of two 3-digit numbers.
"""
# a number which is a product of two 3-digit numbers
# is either 5-digited or 6-digited
# in order to find the largest we start from searching
# through the 6-digit numbers and if we do not find any
# we search among the 5-digit numbers.

#the function tests whether a number is palidrome or not
def IsPalindrome(Num):
    MyStr=str(Num)
    for i in range(0,len(MyStr)//2):
        if MyStr[i]!=MyStr[len(MyStr)-1-i]:
            return False
    return True


Compare=0
for i in range(999,99,-1):
    for j in range(999,99,-1):
        if IsPalindrome(i*j):
            Max=max(i*j,Compare)
            Compare=Max
            break#the break is because we want the max
print(Max)
        
    
    
