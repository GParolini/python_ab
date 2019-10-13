#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 23:46:41 2019

@author: giudittaparolini
"""

class Course:

    def __init__(self, name, ratings): #use of parametrized constructors
        self.name=name
        self.ratings=ratings
#define an instance methods
    def average(self):
        numberOfRatings=len(self.ratings)
        average = sum(self.ratings)/numberOfRatings
        print("Average Ratings for", self.name, "is", average)


c1 = Course ("Java Course", [1,2,3,4,5])
print(c1.name)
print(c1.ratings)
c1.average()

c2 = Course ("Java Web Services", [5,5,5,5])
print(c2.name)
print(c2.ratings)
c2.average()
