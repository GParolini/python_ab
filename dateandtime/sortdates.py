#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 22:05:10 2019

@author: giudittaparolini
"""
from datetime import date
import time

startTime= time.perf_counter()

ldates = []

d1=date(2016, 8, 12)
d2=date(2016, 7, 12)
d3=date(2018, 8, 12)

ldates.append(d1)
ldates.append(d2)
ldates.append(d3)

ldates.sort()

for i in ldates:
    print (i)
    
print ("-----") 
    
time.sleep(3) #temporarily halt the execution of the program

for i in ldates:
    print(i)

endTime= time.perf_counter()

print("Execution Time:", endTime-startTime)