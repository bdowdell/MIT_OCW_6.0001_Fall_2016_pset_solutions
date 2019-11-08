#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 19:16:05 2019

@author: bendowdell
"""

# =============================================================================
# Part B: Saving, with a raise
# Background
# In Part A, we unrealistically assumed that your salary didn’t change. But you are an MIT graduate, and
# clearly you are going to be worth more to your company over time! So we are going to build on your
# solution to Part A by factoring in a raise every six months.
# In ​ ps1b.py​ , copy your solution to Part A (as we are going to reuse much of that machinery). Modify
# your program to include the following
# 1. Have the user input a semi-annual salary raise ​ semi_annual_raise​ (as a decimal percentage)
# 2. After the 6​ th​ month, increase your salary by that percentage. Do the same after the 12 th
# month, the 18​ th ​ month, and so on.
# Write a program to calculate how many months it will take you save up enough money for a down
# payment. LIke before, assume that your investments earn a return of ​ r ​ = 0.04 (or 4%) and the
# required down payment percentage is 0.25 (or 25%). Have the user enter the following variables:
# 1. The starting annual salary (annual_salary)
# 22. The percentage of salary to be saved (portion_saved)
# 3. The cost of your dream home (total_cost)
# 4. The semi­annual salary raise (semi_annual_raise)
# =============================================================================

# =============================================================================
# Test Case 1
# >>>
# Enter your starting annual salary:​ 120000
# Enter the percent of your salary to save, as a decimal: ​ . 05
# Enter the cost of your dream home: ​ 500000
# Enter the semi­annual raise, as a decimal:​ .03
# Number of months:​ 142
# >>>
# Test Case 2
# >>>
# Enter your starting annual salary:​ 80000
# Enter the percent of your salary to save, as a decimal: ​ . 1
# Enter the cost of your dream home: ​ 800000
# Enter the semi­annual raise, as a decimal:​ .03
# Number of months:​ 159
# >>>
# Test Case 3
# >>>
# Enter your starting annual salary:​ 75000
# Enter the percent of your salary to save, as a decimal: ​ . 05
# Enter the cost of your dream home:​ 1500000
# Enter the semi­annual raise, as a decimal:​ .05
# Number of months:​ 261
# =============================================================================

# Begin by getting the basic input from the user

# Ask the user for their annual_salary and cast it as an int
annual_salary = float(input('Enter your annual salary: '))

# Ask the user for the percentage of annual_salary to save
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))

# Ask the user for the cost of the house to purchase
total_cost = float(input('Enter the cost of your dream home: '))

# Ask the user for the semi-annual raise perecentage
semi_annual_raise = float(input('Enter semi-annual raise, as a decimal: '))

# Now calculate how many months it will take to save up for the down payment
portion_down_payment = 0.25*total_cost
current_savings = 0.00

# calculate monthly salary
monthly_salary = annual_salary / 12

# calculate monthly savings
monthly_savings = monthly_salary * portion_saved

# initialize a counter for months
months = 0

# current_savings are invested on a monthly basis with a rate of return r
r = 0.04

# use a while loop to iteratively add to current_savings to determine
# how many months are required to save up to portion_down_payment
# 7. At the end of each month, your savings will be increased by the return on your investment,
# plus a percentage of your ​ monthly salary ​ (annual salary / 12).
while current_savings < portion_down_payment:
    current_savings += (current_savings*r/12) + monthly_savings
    months += 1
    if months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
        monthly_salary = annual_salary / 12
        monthly_savings = monthly_salary * portion_saved
    
print('Number of months: {}'.format(months))