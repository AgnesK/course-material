# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 18:28:45 2014

@author: Agnes
"""
import is_prime
var = 0
for i in range(1000):
    if is_prime.is_prime(i):
        var = var + i
print(var)
