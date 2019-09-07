#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 16:11:05 2019

@author: giudittaparolini
"""
#integer type
a=13
b=100
c=-66
print (a,b,c)
print(type(a))

#floaating point type
x=33.5
y=-25.8
z=205.0
print (x,y,z)
print(type(z))

#complex type
d=3+5j
print(d)
print(type(d))

#binary type
e=0B1010
print(e)
print(type(e))

#exadecimal type
f=0XFF
print(f)
print(type(e))

#octal type
o=0o117
print(o)
print(type(o))

#boolean type
g=True
print(g)
print(type(g))
print(9>8)
print(8>9)

#Convert a type into another
#Example with a floating point number converted into an integer
h=int(x)
print(h)
print(type(h))

#Convert a string
i=float("22.5")
print(i)
print(type(i))

#Convert an integer into a binary number
l=bin(10)
print(l)
print(type(l))

#Convert an integer into an hexadecimal number
m=hex(10)
print(m)
print(type(m))

#Convert an integer into an octal number
n=oct(10)
print(n)
print(type(n))
