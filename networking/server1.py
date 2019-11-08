#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 22:31:03 2019

@author: giudittaparolini
"""


import socket

host = "127.0.0.1"
port= 65432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((host, port))

s.listen(1)
print("Server listening on port:", port)

c, addr = s.accept()

fileName = c.recv(1024)

try:
    open(fileName, 'rb')
    content = fileName.read()
    c.sendall(content)
    fileName.close()
except FileNotFoundError:
    c.sendall(b"File does not exist")

c.close()