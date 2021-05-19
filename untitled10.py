# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 18:51:06 2021

@author: kalya
"""

def list(a_list):
    return [a_list[0], a_list[len(a_list)-1]]

while a_list ==exit:
    a_list = int(input("Enter the number list:"))
    
print(list(a_list))