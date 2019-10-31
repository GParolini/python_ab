#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 23:38:02 2019

@author: giudittaparolini
"""

import pickle
f=open("student.dat", "rb")

obj = pickle.load(f)
obj.display()
f.close()