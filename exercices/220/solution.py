# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 18:28:45 2014

@author: Agnes
"""
import is_prime
var = ''
for i in range(10000, 10050):
    if is_prime.is_prime(i):
        if var == '':
            var = str(i)
        else:
            var = str(var) + ', ' + str(i)
var = str(var)
print(var)
