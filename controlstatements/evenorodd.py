#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 12:04:12 2019

@author: giudittaparolini
"""
# without the 0 case
"""
x = int((input("Enter a number:"))

if x%2 == 0:
    print(x, " is even")
else:
    print(x, " is odd")
    
"""

#adding the 0 case
"""
x = int(input("Enter a number:"))

if x == 0:
    print(x, "is zero")

elif x%2 == 0:
    print(x, " is even")

else:
    print(x, " is odd")
    
"""

#adding the float input case

x = input("Enter a number:")
x1 = float(x)
x2 = int(x1)

if x2 == 0:
    print(x1, "is zero")

elif x2%2 == 0:
    print(x2, " is even")

else:
    print(x2, " is odd")


#you can also have the case where you round the given number

"""
x = input("Enter a number:")
x1 = round(x)
x2 = int(x1)

if x2 == 0:
    print(x1, "is zero")

elif x2%2 == 0:
    print(x2, " is even")

else:
    print(x2, " is odd")
    
"""