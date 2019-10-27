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
    
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def drive(self):
        pass

class ThreeSeries(BMW):
    
    def __init__(self, cruiseControlEnabled, make, model, year):
        super().__init__(make, model, year)
        self.cruiseControlEnabled = cruiseControlEnabled
    
    def display(self):
        print(self.cruiseControlEnabled)
        
    def start(self):
        super().start()
        print ("Button Start")
    
    def stop(self):
        super().stop()
        print ("Button Stop")
        
    def drive(self):
        print("Three Series is being driven")

class FiveSeries(BMW):
    
    def __init__(self, parkingAssistEnabled, make, model, year):
        super().__init__(make, model, year)
        self.parkingAssistEnabled = parkingAssistEnabled
        
    def drive(self):
        print("Five Series is being driven")
    def start(self):
        super().start()
        print ("Remote Start")
    
    def stop(self):
        super().stop()
        print ("Remote Stop")
    def display(self):
        print(self.cruiseControlEnabled)
        

ThreeSeries=ThreeSeries(True, "BMW", "328i", "2018")
print(ThreeSeries.cruiseControlEnabled)
print(ThreeSeries.make)
print(ThreeSeries.model)
print(ThreeSeries.year)

ThreeSeries.start()
ThreeSeries.stop()
ThreeSeries.drive()
ThreeSeries.display()

print ("------")

FiveSeries = FiveSeries(True, "BMW", "G30", "2017")
print(FiveSeries.parkingAssistEnabled)
print(FiveSeries.make)
print(FiveSeries.model)
print(FiveSeries.year)

FiveSeries.start()
FiveSeries.stop()
FiveSeries.drive()
