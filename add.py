#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""CodeFights The Journey Begins
        add"""
# Function Definition
def add(param1, param2):
    return float(param1) + float(param2)
#Get input
print("Adds a and b")
num1 = input("a = ? ")
num2 = input("b = ? ")
#Execute add()
answer = add(num1, num2)
#Print the answer
print("Answer: %2.0f"% answer)
