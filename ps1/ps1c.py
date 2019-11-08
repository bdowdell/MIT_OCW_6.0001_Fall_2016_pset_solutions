#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 23:04:55 2019

@author: bendowdell
"""

# Print an introductory line
print('You want to purchase a $1MM home.  In order to do so, you first need')
print('to save up 25%, and wish to do so in 36 months.  This program will')
print('determine what amount of monthly salary should be saved to meet this goal')

# Begin by getting the basic input from the user
# Ask the user for their annual_salary and cast it as an int
init_annual_salary = float(input('Enter your annual salary: '))

# Set the fixed variables
semi_annual_raise = 0.07
r = 0.04
percent_down_payment = 0.25
total_cost = 1000000.00

# Now calculate how many months it will take to save up for the down payment
portion_down_payment = percent_down_payment*total_cost
current_savings = 0.00

# initialize a counter for months
months = 0

# Use bisection search to find the optimal savings rate
low = 0
high = 10000
guess = (low + high)//2
steps = 0
epsilon = 100.0 # want the solution to be within $100 of down payment
annual_salary = init_annual_salary
loop = True
while loop:
    while (portion_down_payment - current_savings) > epsilon:
        current_savings += (current_savings*(r/12)) + (annual_salary/12)*(guess/10000)
        months += 1
        if months % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise
    if months > 36:
        # need to save at a higher rate
        low = guess
        # reset variables
        months = 0
        annual_salary = init_annual_salary
        current_savings = 0
    elif months < 36:
        # saving too agressively
        high = guess
        # reset variables
        months = 0
        annual_salary = init_annual_salary
        current_savings = 0
    else:
        # Goldilocks!  We have found the optimal rate to save in 36 months
        optimumRate = guess / 10000
        possible = True
        loop = False
    steps +=1
    guess = (low + high)//2
    if guess == 9999:
        # it is not possible to save in three years
        possible = False
        loop = False

# Print the results
if possible:
    print('Best savings rate: ', optimumRate)
    print('Steps in bisection search: ', steps)
else:
    print('At this salary, it is not possible to save the down payment in 36 months.')
        

