#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 22:42:34 2019

@author: giudittaparolini
"""

def display(name):
    def message ():
        return "Hello "
    result = message() + name
    return result


print(display ('Giuditta'))

#print(message()) trhows an error