# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 11:55:33 2014

@author: Agnes
"""
var = 0
for i in range(1000):
    if i % 3 == 0:
        var = var + i
    elif i % 5 == 0:
        var = var + i
print(var)
