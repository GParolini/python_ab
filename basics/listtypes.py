#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 12:13:09 2019

@author: giudittaparolini
"""

lst=[]
print(lst) #empty list

lst1=[10,20, "Giuditta", -10, 30.5] #list with elements
print(lst1)
print(lst1[3]) #select elements to print

#slicing
print(lst1[3:5])

#repetition
print(lst1*4)

#length
print(len(lst1))

#add, remove, delete
lst1.append(40)
lst1.remove("Giuditta") #capital sensitive
del(lst1[1])
print(lst1)

#lst1.clear()
#print(lst1)

#max value
max(lst1)
print(max(lst1))

#min value
min(lst1)
print(min(lst1))

#insert 99 at index 3
lst1.insert(3,99)
print(lst1)

#sort
lst1.sort()
lst1.sort(reverse=True)
print(lst1)