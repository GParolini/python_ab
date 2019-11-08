#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 22:28:20 2019

@author: giudittaparolini
"""

import threading

print("Current Thread that is running: ", threading.current_thread().getName())

if threading.current_thread() == threading.main_thread():
    print("Main Thread")
else:
    print("Some other thread")