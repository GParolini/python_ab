#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 15:44:32 2019

@author: giudittaparolini
"""

class Flight:
    def __init__(self, engine):
        self.engine = engine
    
    def startEngine(self):
        self.engine.start();

class AirbusEngine:
    def start(self):
        print("Starting Airbus engine")
        

class BoingEngine:
    def start(self):
        print("Starting Boing engine")
        
        
        
ae= AirbusEngine()
f = Flight(ae)
f.startEngine()

be= BoingEngine()
f = Flight(be)
f.startEngine()