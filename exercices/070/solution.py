# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 11:55:33 2014

@author: Agnes
"""
str = "abcdefghijklmnopqrstuvwxyz"
for i in str:
    for j in str:
        if i != j:
            print(i + j)
