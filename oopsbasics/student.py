#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 21:44:07 2019

@author: giudittaparolini
"""

class Student:
    major = "CSE" #major is a static field, i.e. class-level field

    def __init__(self,rollno, name):
        self.rollno=rollno
        self.name=name


s1=Student(1,"John")
s2=Student(2,"Bill")

print(s1.major)
print(s2.major)
print(s1.name)
print(s2.name)
print(Student.major)
