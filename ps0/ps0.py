# -*- coding: utf-8 -*-
"""
Pset 0
Write a programe that does the follwing in order:
1. Asks the user to enter a number "x"
2. Asks the user to enter a number "y"
3. Prints out number "x", raised to the power "y"
4. Prints out log (base 2) of "x"
"""

# 1. Ask for the user to enter a number
# Assign the input to variable "x"
x = input('Please enter a number, "x": ')

# 2. Ask for the user to enter a second number
# Assign the input to variable "y"
y = input('Please enter a number, "y": ')

# Type cast the input from string to int
x = int(x)
y = int(y)

# print out "x" raised to the power "y"
print('x**y = ', x**y)

# Print out log2(x)
from numpy import log2

print('log2(x) = ', log2(x))
