# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 13:04:46 2018

@author: 段江飞
"""
annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))
semi_annual_raise = float(input('Enter the semi-annual raise, as a decimal: '))

portion_down_payment = 0.25
current_savings = 0.0
r = 0.04
i = 0
while current_savings < total_cost * portion_down_payment:
    i = i + 1
    current_savings += (current_savings * r + portion_saved * annual_salary) / 12
    annual_salary = annual_salary + (i % 6 == 0) * annual_salary * semi_annual_raise

print('Number of months: ', i)