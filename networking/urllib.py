#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 21:49:02 2019

@author: giudittaparolini
"""

import urllib.request

try:
    url = urllib.request.urlopen("https://www.python.org")
    content = url.read()
except urllib.error.HTTPError:
    print("Web Page not found")
    exit()

f = open("python.html", "wb")
f.write(content)
f.close()