# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 18:28:45 2014

@author: Agnes
"""
import is_prime
var = 14
b = True
while b:
    print(is_prime.is_prime(var))
    if is_prime.is_prime(var):
        b = False
    else:
        var = var + 1
print(var)
