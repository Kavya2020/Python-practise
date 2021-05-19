# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 22:48:27 2021

@author: kalya
"""
n = str(input("Enter a long string containing multiple words:"))
result = n.split(" ")
reversedstring = ' '.join(reversed(result))
print(reversedstring)

