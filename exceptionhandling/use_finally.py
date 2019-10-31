#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 08:20:56 2019

@author: giudittaparolini
"""

try:
    f = open("myfile", "w")

    a, b = [int(x) for x in input("Enter two numbers: ").split()]
    c = a/b 
    f.write("Writing %d into file" %c)


except ZeroDivisionError:
    print("Division by zero is not allowed")
    print("Please enter a non zero numbers")

else:
    print("You have entered a non zero number")

finally:
    f.close()
    print("File closed")

print("Code after the exception")