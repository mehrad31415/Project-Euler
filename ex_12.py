# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 00:26:21 2021

@author: Daneshjoei
"""
"""example 12:
    What is the value of the first triangle number to 
    have over five hundred divisors?
"""
#the function gives the number of divisors of Num
def NumOfDivisors(Num):
    Multi=1
    #f=0
    for i in range (2,Num+1):
        counter=1
        while Num%i==0:
            Num=Num//i
            counter+=1
            if Num==1:
                Multi*=counter
                return Multi
        #f+=1
        #print(f)
        #f gives the number of sequences that of the
        #for-loop
        Multi*=counter
    #if we write return Multi here the num of sequences
    #for 28 will be 27 but when we write it there it
    #will be 5 times only!!! try it by testing f

#print (NumOfDivisors(28))

def TriangleNum(Num):
    return int((Num*(Num+1))/2)

Num=2
while True:
    if NumOfDivisors(TriangleNum(Num))>500:
        print (TriangleNum(Num))
        break
    Num+=1



        
        