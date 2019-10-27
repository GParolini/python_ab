#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 23:50:33 2019

@author: giudittaparolini
"""

from abc import abstractmethod, ABC

class BMW(ABC):
    
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def start(self):
        print ("Starting the car")
        
    def stop(self):
        print ("Stopping the car")

    @abstractmethod
    def drive(self):
        pass

class ThreeSeries(BMW):
    
    def __init__(self, cruiseControlEnabled, make, model, year):
        #BMW.__init__(self, make, model, year)
        super().__init__(make, model, year)
        self.cruiseControlEnabled = cruiseControlEnabled
    
    def display(self):
        print(self.cruiseControlEnabled)
        
    def start(self):#overrides the method in the parent class by definying a new one, with the same name, for the child class
        super().start()#invokes the parent class' method 
        print ("Button Start")
    
    def drive(self):
        print("Three Series is being driven")

class FiveSeries(BMW):
    
    def __init__(self, parkingAssistEnabled, make, model, year):
        #BMW.__init__(self, make, model, year)
        super().__init__(make, model, year)
        self.parkingAssistEnabled = parkingAssistEnabled
        
    def drive(self):
        print("Five Series is being driven")
    

bmw=ThreeSeries(True, "BMW", "328i", "2018")
print(bmw.cruiseControlEnabled)
print(bmw.make)
print(bmw.model)
print(bmw.year)

bmw.start()
bmw.stop()
bmw.display()
bmw.drive()

print ("------")

bmw = FiveSeries(True, "BMW", "G30", "2017")
print(bmw.parkingAssistEnabled)
print(bmw.make)
print(bmw.model)
print(bmw.year)

bmw.start()
bmw.stop()
bmw.drive()