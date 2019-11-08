#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 21:56:09 2019

@author: giudittaparolini
"""

from datetime import *

d =date(2019,11,1)
t = time (21, 57, 00)
dt = datetime.combine(d,t)
print(dt)