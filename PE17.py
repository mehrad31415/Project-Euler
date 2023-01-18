#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 11:08:48 2022

@author: mehradhq
"""
"""
problem 17: 
    If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
    then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

    If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
    how many letters would be used?


    NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
    contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
    The use of "and" when writing out numbers is in compliance with British usage.
    d={1:"one",#3
       2:"two", #3
       3:"three",#5
       4:"four",#4
       5:"five",#4
       6:"six",#3
       7:"seven",#5
       8:"eight",#5
       9:"nine",#4
       10:"ten",#3
       11:"eleven",#6
       12:"twelve",#6
       13:"thirteen",#8
       14:"fourteen",#8
       15:"fifteen",#7
       16:"sixteen",#7
       17:"seventeen",#9
       18:"eighteen",#8
       19:"nineteen",#8
       20:"twenty",#6
       30: "thirty",#6
       40:"forty",#5
       50:"fifty",#5
       60:"sixty",#5
       70:"seventy",#7
       80:"eighty",#6
       90:"ninety",#6
       100:"hundred",#7
       }
"""
three=[1,2,6]
four=[4,5,9]
five=[3,7,8]
six_ten=[11,12]
seven_ten=[15,16]
eight_ten=[13,14,18,19]

s=0
for i in range (1,1000):
    # first we check if the number is like 11 or 12... 19 because if we do it other way around
    #and first check modulo 10 we will not get this
    if i%100 in six_ten:
        s+=6
    elif i%100 in seven_ten:
        s+=7
    elif i%100 in eight_ten:
        s+=8
    elif i%100==17:
        s+=9
    elif i%100==10:
        s+=3
    else:
        #counting the forty, fifty ....the tenth.
        if 20<=i%100<40 or 80<=i%100:
            s+=6
        elif 40<=i%100<70:
            s+=5
        elif 70<=i%100:
            s+=7
        #chcking the lowest priority number and counting that
        if i%10 in three:
            s+=3
        elif i%10 in four:
            s+=4
        elif i%10 in five:
            s+=5
    #checking the property of numbers above 100
    if i>=100:
        #checking hundred and "and" in a number and counting them.
        if i%100!=0:
            s+=10#and
        else:
            s+=7
        #counting "one" hundred, "two" hundred, that is the prefix of hundred
        if i//100 in three:
            s+=3
        elif i//100 in four:
            s+=4
        elif i//100 in five:
            s+=5
#one thousand=11
#the range is inculsive so we have to add one thousand as well.
print (s+11)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        
        