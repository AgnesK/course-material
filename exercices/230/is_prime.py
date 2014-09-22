# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 18:28:45 2014

@author: Agnes
"""


def is_prime(a):
    if a == 2:
        return(True)
    else:
        for i in range(2, a):
            if a % i == 0:
                return(False)
    return(True)
