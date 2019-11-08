#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 22:00:04 2019

@author: giudittaparolini
"""

import socket

host = "localhost"
port= 4000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))

s.listen(1)
print("Server listening on port:", port)

c,addr = s.accept()

print("Connection from: ", str(addr))

c.send("Hello, how are you".encode())
c.send ("bye".encode())
c.close()