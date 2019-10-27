#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 09:55:11 2019

@author: giudittaparolini
"""
from abc import abstractmethod, ABC

class TouchScreenLaptop(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    @abstractmethod
    def scroll(self):
        pass
    
    @abstractmethod
    def click(self):
        pass
    

class HP(TouchScreenLaptop):  
    def scroll(self):
        print ("HP Scrolling")
    
    
class DELL(TouchScreenLaptop):
    def scroll(self):
        print ("DELL Scrolling")


class HPNotebook(HP):
    def click(self):
        print ("HP Click")
    
    
class DELLNotebook(DELL):
    def click (self):
        print ("DELL Click")

hp= HPNotebook("HP", "Model hp xyz")
d= DELLNotebook("DELL", "Model dell xxx")

print(hp.brand)
print(hp.model)
hp.click()
hp.scroll()

print ("-----")


print(d.brand)
print(d.model)
d.click()
d.scroll()