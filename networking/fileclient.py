#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 22:44:08 2019

@author: giudittaparolini
"""

import socket

s = socket.socket()

s.connect(("127.0.0.1", 65432))

fileName = input ("Enter a file name:")

s.send(fileName.encode())
content = s.recv(1024)

print(content.decode())

s.close()