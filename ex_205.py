# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 22:51:51 2021

@author: Daneshjoei
"""

"""example 205:
    Peter has nine four-sided (pyramidal) dice,
    each with faces numbered 1, 2, 3, 4.
    Colin has six six-sided (cubic) dice,
    each with faces numbered 1, 2, 3, 4, 5, 6.

    Peter and Colin roll their dice and compare totals:
    the highest total wins. The result is a draw if
    the totals are equal.

    What is the probability that Pyramidal Pete beats
    Cubic Colin? Give your answer rounded to seven decimal
    places in the form 0.abcdefg
"""
#peter:x1+...+x9=(9-36)
#colin:x1+...+x6=(6-36)

#the function below gives the factoriel of Num
def factoriel(Num):
    if Num==0 or Num==1:
        return 1
    prod=1
    for i in range (2,Num+1):
        prod*=i
    return prod
#the function below gives combinations
def combinations(Num,iter):
    if Num<iter:
        return 0
    return factoriel(Num)/(factoriel(iter)*factoriel(Num-iter))
#the function below gives the number of ways that peter
#can have a total sum of "Num" with his dices
def SumPeter(Num):
    total=combinations(Num-1,8)
    for i in range (4,Num+1,4):
        if Num-1-i<8:
            return total
        total+=(((-1)**(i//4))*combinations(Num-1-i,8)*combinations(9,(i//4)))
#the fnction below gives the number of ways that colin
#can have a total sum of "Num" with his dices
def SumColin(Num):
    total=combinations(Num-1,5)
    for i in range (6,Num+1,6):
        if Num-1-i<5:
            return total
        total+=(((-1)**(i//6))*combinations(Num-1-i,5)*combinations(6,(i//6)))
Total=0
for i in range (9,37):
    S=0
    for j in range (6,i):
        S+=SumColin(j)
    Total+=(SumPeter(i)*S)
denominator=(6**6)*(4**9)
print (Total/denominator)
    
        