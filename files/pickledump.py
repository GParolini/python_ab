#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 23:33:37 2019

@author: giudittaparolini
"""

import pickle
import student

f = open ("student.dat", "wb")
s = student.Student(123, "John", 90)

pickle.dump(s, f)
f.close()