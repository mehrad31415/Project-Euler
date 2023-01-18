# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 09:47:56 2021

@author: Daneshjoei
"""

"""example3:
      The largest prime factor (lpf) of 600851475143?
"""

def LPF(Num):
    for i in range(2,Num):
        while Num%i==0:
            Num=Num//i
            if Num==1:
                return Num*i
print(LPF(600851475143))

