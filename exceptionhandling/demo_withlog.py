#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 08:20:56 2019

@author: giudittaparolini
"""

import logging

logging.basicConfig(filename="mylogdemo.log", level=logging.DEBUG)

try:
    f= open("myfile.txt", "w")
    a, b = [int(x) for x in input("Enter two numbers: ").split()]
    logging.info("Division in progress")
    c = a/b 
    f.write("Writing %d into file" %c)
    

except ZeroDivisionError:
    print("Division by zero is not allowed")
    print("Please enter a non zero numbers")
    logging.error("Division by zero")
    
else:
    print("You have entered a non zero number")
finally:
    f.close()
    print("File closed")

print("Code after the exception")