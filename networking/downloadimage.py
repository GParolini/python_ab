#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 21:56:22 2019

@author: giudittaparolini
"""

import urllib.request
url = "https://www.python.org/static/img/python-logo@2x.png"

urllib.request.urlretrieve(url, "pythonlogo.png")
