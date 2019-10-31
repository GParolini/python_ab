#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 09:28:47 2019

@author: giudittaparolini
"""

#The online course is missing a piece, as there is no explanation of how to build a custom exception. A search on Google helped to fill in the gap.

class InvalidPasswordException(Exception):
    pass
        
class PasswordTooShort(InvalidPasswordException):
    pass
    
try:
    p = str(input("Input your password: "))
    if len(p)<8:
        raise PasswordTooShort
    print("Your password is: %s " %p)
    
except:
    print("Error. Your password must have at least 8 characters. Input a new password")
    
