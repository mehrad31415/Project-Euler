# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 21:08:28 2021

@author: Daneshjoei
"""
"""example 14:
    The following iterative sequence is defined for the 
    set of positive integers:
                                n → n/2 (n is even)
                                n → 3n + 1 (n is odd)

    Using the rule above and starting with 13,
    we generate the following sequence:
        13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
    It can be seen that this sequence 
    (starting at 13 and finishing at 1) contains 10 terms.
    Although it has not been proved yet (Collatz Problem),
    it is thought that all starting numbers finish at 1.
    Which starting number, under one million,
    produces the longest chain?
"""
#the function gives the number of terms         
def NumOfSequenceCollatzProblem(Num):
    counter=0
    while Num>1:
        if Num%2==0:
            Num=Num//2
        else:
            Num=(3*Num)+1
        counter+=1
    return counter+1

#test:print (NumOfSequenceCollatzProblem(13))

Max=0
#all the numbers below 500,000 can b multiplied by a power
#of two so that they are more than 500,000 and obviously 
#the number of terms in the Collatz Problem is more. 
for i in range (500001,1000000,2):
    if NumOfSequenceCollatzProblem(i)>Max:
        Max=NumOfSequenceCollatzProblem(i)
        NumberMostTerms=i
print (Max,NumberMostTerms)

    