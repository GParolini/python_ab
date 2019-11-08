#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 21:41:42 2019

@author: giudittaparolini
"""

import time
import datetime

epochsec = time.time()
print(epochsec)

t = time.ctime(epochsec)
print(t)

dt = datetime.datetime.today()
print(dt)
print(dt.day, dt.month, dt.year)
print('Current Date: {}/{}/{}'.format(dt.day, dt.month, dt.year))
print('Current Time: {}:{}:{}'.format(dt.hour, dt.minute, dt.second))