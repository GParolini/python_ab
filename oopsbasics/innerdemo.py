#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 22:27:11 2019

@author: giudittaparolini
"""
# Create an inner class
class Car:
    def __init__(self, make, year):
        self.make= make
        self.year= year
        
    class Engine:
        def __init__(self, number):
            self.number = number
        def start(self):
            print("Engine started")

c = Car("BMV", 2017)
e = c.Engine(123)
e.start()