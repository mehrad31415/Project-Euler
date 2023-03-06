#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 11:04:45 2022

@author: mehradhq
"""

a="123+2/5-7"
"""
"a" is a string. contaning only mathematical operations *, +, -, /.
beside the operations it has numbers.
no other element such as symbols and spaces are present in our string.
we want to calculate the operation written in the string
suchas the priority in mathematical operations does not exist.
that is the operations regardless of their priority are carried out
from left to right.

"""
#the below are the function for mathematical operations.
def multiply(num1,num2):
    return num1*num2
def add(num1,num2):
    return num1+num2
def subtract(num1,num2):
    return num1-num2
def divide(num1,num2):
    return num1/num2
#this is our list of numbers from 0-9
b=[i for i in range (10)]
#below is a dictionary which indicates what symbols do in the string.
operation={"*":multiply,"+":add,"-":subtract,"/":divide}

#s is an empty string to add our string numbers to
s=""
counter=0
for i in range (len(a)):
    for j in operation:
        if j==a[i]:
            counter+=1
            if counter>1:
                num2=int(s)
                result=operation[temporary](num1,num2)
                num1=result
                temporary=j
                s=""
                break
            else:
                temporary=j
                num1=int(s)
                s=""
                break
    else:   
        s+=a[i]
        
# the below line is only for when after the last digit there is not other operation.
if len(s)>0:
    num2=int(s)
    result=operation[temporary](num1,num2)
    print (result)
        
        
        

