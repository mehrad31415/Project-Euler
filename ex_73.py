# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 17:59:16 2021

@author: Daneshjoei
"""
"""example 73:
    How many fractions lie between 1/3 and 1/2 in the 
    sorted set of reduced proper fractions for d ≤ 12,000?
"""

def gcd(Num1,Num2):
    assert Num1<=Num2 and Num1>=0
    if Num1==0 and Num2==0:
        return "No possible answer"
    while Num1!=0:
        Temp=Num1
        Num1=Num2%Num1
        Num2=Temp
    return Num2
 
   
def CoPrime(Num1,Num2):
    if gcd(Num1,Num2)==1:
        return True

counter=0
for d in range (2,12001):
    for i in range ((d//3)+1,(d//2)+1):
        if CoPrime(i,d):
            #print (i/d)
            counter+=1
print (counter-1)
#the above range makes sure that the number is more than
#1/3 but does not make sure that the number is below 1/2
#for that purpose the CoPrime(i,d) takes care of it; how?
#take d=10 the range includes:5,4 but but 5 and 10 are not
#coprime so it will not be included and for d odd number
#the range is always below 1/2. Now the only fraction which
#is included is 1/2 which is not below 1/2 and is also
#coprime so we have to declude this fraction from the whole