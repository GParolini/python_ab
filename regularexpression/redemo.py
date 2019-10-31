#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 23:40:24 2019

@author: giudittaparolini
"""
#search returns only the first instance
import re
str1 = "Take up one idea. One idea at a time"

result = re.search(r'o\w\w',str1)
print(result.group())

result = re.search(r'o\w',str1)
print(result.group())


str2 = "Take up one idea. one idea at a time"

result = re.findall(r'o\w\w',str2)
print(result)

result = re.findall(r'o\w\w',str1)
print(result)

str3 = "Take up One idea. One idea at a time"
result = re.findall(r'o\w\w',str3)
print(result)

result = re.match(r'o\w\w',str3)
print(result)

result = re.match(r'T\w\w',str3)#match only returns the first instance. The matching starts at the beginning of the string
print(result.group())

str4 = "Take 1 up One 23 idea. One idea 45 at a Time"

result = re.split (r'\d+', str4)
print(result)

result = re.sub (r'One', 'Two', str3)
print(result)

result = re.findall (r'O\w+', str3)
print(result)

result = re.findall (r'O\w*', str3)
print(result)

result = re.findall (r'O\w?', str3)
print(result)

result = re.findall (r'O\w{1}', str3)
print(result)

str5 = "Take up One idea. Only One idea at a time"
result = re.findall (r'O\w{3}', str5)
print(result)

result = re.findall (r'O\w{1,2}', str3)
print(result)

str6 = "Take 1 up 1-3-2019 One 23 idea. One idea 45 at a Time 12-11-2020"

result = re.findall (r'\d{1,2}-\d{1,2}-\d{4}', str6)
print(result)

result = re.search(r'^O\w', str6) #With the ^ symbol the match is done right at the beginning of the string
print(result)

result = re.search(r'^T\w', str6)
print(result.group())

result = re.search(r'^T\w*', str6)
print(result.group())