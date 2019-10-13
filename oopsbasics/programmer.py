#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 21:37:13 2019

@author: giudittaparolini
"""
#getter and setter methods
class Programmer:
    def setName(self,name):
        self.name=name

    def getName(self):
        return self.name

    def setSalary(self, salary):
        self.salary = salary

    def getSalary(self):
        return self.salary

    def setTechnologies(self, technologies):
        self.technologies = technologies

    def getTechnologies(self):
        return self.technologies


p1 = Programmer()

p1.setName("John")
p1.setSalary(10000)
p1.setTechnologies(["Java", "Hibernate", "Spring", "Python"])

print(p1.getName())
print(p1.getSalary())
print(p1.getTechnologies())
