#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 22:23:43 2019

@author: giudittaparolini
"""
#count the number of objects in a class
class ObjectCounter:

    numberOfObjects = 0
    def __init__(self):
        ObjectCounter.numberOfObjects +=1

    @staticmethod
    def displayCount():
        print(ObjectCounter.numberOfObjects)


a1= ObjectCounter()
a2= ObjectCounter()

ObjectCounter.displayCount()
