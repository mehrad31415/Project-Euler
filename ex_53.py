# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 11:39:34 2021

@author: Daneshjoei
"""
"""example 53:
    How many, not necessarily distinct, values of 
    combinations(n,r) for 1<=n<=100, are greater than
    one-million?
"""
#the below function gives Num!: the product of
#all numbers below and equal to Num
def factoriel(Num):
    if Num==0 or Num==1:
        return 1
    prod=1
    for i in range (2,Num+1):
        prod*=i
    return prod
#the function below is the formula for calculating
#the combinations of (Num,r)
def combinations(Num,r):
    return factoriel(Num)/(factoriel(r)*factoriel(Num-r))

#below is for calculating for even numbers and the second
#one is for odd numbers; this is instead of using
#Num%2==0 or Num%2!=0 which makes our algorithm quicker.
#the reason for dividing odd and even numbers is that for
#even numbers we have (20,10) but for odd there is
#(21,10) and (21,11)
#we only count up until the half of n and add the counter by2
#the reason for this is pascals theorem:
    #(n,r)=(n,n-r)so if the each is bigger than 
    #10^6 the other one is too.
# we start our r range from 4 because for 3
#the biggest n is 100 which in the numenator 
#we have 100*99*98 is already smaller than 10^6
#for this reason we start n from 8 given that for no
#n<8 (n,r) is bigger than 10^6
counter1=0       
for n in range (8,101,2):
    for r in range (4,(n//2)):
        if combinations(n,r)>1000000:
            counter1+=2
    if combinations(n,n//2)>1000000:
        counter1+=1
        
counter2=0        
for n in range (9,100,2):
    for r in range (4,(n//2)+1):
        if combinations(n,r)>1000000:
            counter2+=2
print (counter1+counter2)    