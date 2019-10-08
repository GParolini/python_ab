#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  7 22:02:00 2019

@author: giudittaparolini
"""


def decorfun(fun):
    def inner(n):
        result = fun(n)
        result += " How are you?"
        return result
    return inner

@decorfun
def hello(name):
    return "Hello "+name


print(hello("John"))