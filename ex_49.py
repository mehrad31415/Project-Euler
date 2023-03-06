"""
Problem 49: prime permutations:
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
"""

from math import sqrt
from itertools import permutations

def prime(n):
    for i in range (2,int (sqrt(n))+1):
        if n % i == 0:
            return False
    return True

def permutePrime(n):
    l=[]
    s = str(n)
    for p in permutations(s):
        k = int(''.join(p))
        if prime(k):
            l.append(k)
    """
    does the same thing as above.
    for i in permutations(s):
        k = ""
        for j in i:
            k+=j
        if prime(int(k)):
            l.append(int(k))
    """
    return list(set(l))

def find(l):
    if len(l) <=3:
        return
    for i in range (len(l)):
        for j in range (i+1,len(l)):
            if 2* l[j]-l[i] in l:
                if numOfDig(l[i])==4 and numOfDig(l[j]) == 4:
                    return (l[i],l[j],2* l[j]-l[i])

def numOfDig (n):
    """
    if n<10:
        1
    return 1 + numOfDig(n//10)
    """
    c=1
    while n>=10:
        n =n //10
        c +=1
    return c

for i in  range (1000, 9999):
    if prime(i):
        print(find(permutePrime(i)))
