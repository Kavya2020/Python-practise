# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 18:32:21 2021

@author: kalya
"""
num = int(input("Enter a number:"))
def primenumber(num):
    if num%2 == 0:
        print(f"{num} is prime number")
        
    else:
        print(f"{num} is not a prime number")
    return num
primenumber(num)