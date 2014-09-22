# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 10:41:05 2014

@author: Agnes
"""
import sys
if len(sys.argv) < 3:
    print("usage: python3 solution.py OP1 OP2")
else:
    var = float(sys.argv[1]) + float(sys.argv[2])
    print(var)
