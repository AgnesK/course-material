# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 11:55:33 2014

@author: Agnes
"""
str = "abcdefghijklmnopqrstuvwxyz"
count = 0
for i in str:
    count = count + 1
    for j in str[count:]:
        if i != j:
            print(i + j + "\n")
