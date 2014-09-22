# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 18:28:45 2014

@author: Agnes
"""
a = 1
b = 2
text = str(a) + ', ' + str(b)
end = 8
for i in range(end):
    if i != end:
        text = str(text) + str(a + b) + ', '
    else:
        text = str(text) + str(a + b) + '.'
print(str(text))
