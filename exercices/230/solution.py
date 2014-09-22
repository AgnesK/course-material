# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 18:28:45 2014

@author: Agnes
"""
import is_prime
var = 100000000
b = True
while b:
    if is_prime.is_prime(var):
        b = False
    else:
        var = var + 1
print(var)
