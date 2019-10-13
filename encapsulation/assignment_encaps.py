#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 10:04:26 2019

@author: giudittaparolini
"""

class Patient:
    
    def setId(self, iden):
        self.iden = iden
    
    def getId(self):
        return self.iden
    
    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name
    
    def setSsn(self, ssn):
        self.ssn = ssn
    
    def getSsn(self):
        return self.ssn

p = Patient()
p.setId(100456)
p.setName("Bob")
p.setSsn(345678)

print(p.getId())
print(p.getName())
print(p.getSsn())