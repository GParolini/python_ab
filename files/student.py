#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 23:31:57 2019

@author: giudittaparolini
"""

class Student:
    def __init__(self, id, name, testscore):
        self.id = id
        self. name = name
        self.testscore = testscore
        
    def display(self):
        print(self.id, self.name, self.testscore)