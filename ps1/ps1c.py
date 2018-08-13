# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 13:04:46 2018

@author: 段江飞
"""
annual_salary_initial = float(input('Enter the start salary: '))
total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment = 0.25
r = 0.04
#initial portion save rate
portion_saved_high = 2.0
portion_saved_low = 0.0
portion_saved = 1.0
steps = 0
while portion_saved <= 1.0 and portion_saved_low <= portion_saved_high:
    portion_saved = (portion_saved_high + portion_saved_low) / 2;
    steps = steps + 1
    #initial values
    i = 0
    current_savings = 0.0
    annual_salary = annual_salary_initial
    #compute current savings
    while i < 36:
        i = i + 1
        current_savings += (current_savings * r + portion_saved * annual_salary) / 12
        annual_salary = annual_salary + (i % 6 == 0) * annual_salary * semi_annual_raise
    
    delta = current_savings - total_cost * portion_down_payment
    if delta >= 100:
        portion_saved_high = portion_saved
    elif delta < 0:
        portion_saved_low = portion_saved
    else:
        break

if portion_saved <= 0 or portion_saved > 1:
    print('It is not possible to pay down payment in three years.')
else:
    print('Best saving rate:', round(portion_saved, 4))
    print('Steps in bisection search:', steps)