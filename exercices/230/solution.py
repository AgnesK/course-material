# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 18:28:45 2014

@author: Agnes
"""
import is_prime
var = 100000000
b = False
while not b:
    if not is_prime.is_prime(var):
        var = var + 1
    else:
        b = True
print(var)
