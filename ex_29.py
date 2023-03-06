# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 12:38:51 2021

@author: Daneshjoei
"""
"""example 29:
    How many distinct terms are in the sequence 
    generated by ab for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?
"""
def power (Base, Power):
    return Base**Power

MySet=set()
for i in range (2,101):
    for j in range (2,101):
        MySet.add(power(i, j))
#sets do not have repetitive elements
print (len(MySet))
        