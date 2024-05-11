# -*- coding: utf-8 -*-
"""
Schuler, Emalee 

AC0 580

Programming Assignment 1
"""
#Write a program that computes the income tax according to this schedule.


# 1 percent on the first $50,000.
# 2 percent on the amount over $50,000 up to $75,000.
# 3 percent on the amount over $75,000 up to $100,000.
# 4 percent on the amount over $100,000 up to $250,000.
# 5 percent on the amount over $250,000 up to $500,000.
# 6 percent on the amount over $500,000.

# Initialize constant variables for the tax rates and limits. 

RATE_1 = 0.01
RATE_2 = 0.02
RATE_3 = 0.03
RATE_4 = 0.04
RATE_5 = 0.05
RATE_6 = 0.06

RATE_1_LIMIT = 50000.00
RATE_2_LIMIT = 75000.00
RATE_3_LIMIT = 100000.00
RATE_4_LIMIT = 250000.00
RATE_5_LIMIT = 500000.00

# Read income

income = float(input("Enter income: "))

# Compute income tax due
    
if income <= RATE_1_LIMIT:
    incomeTax = RATE_1 * income
    
elif income <= RATE_2_LIMIT:
    incomeTax = RATE_1 * RATE_1_LIMIT + RATE_2 * (income - RATE_1_LIMIT)
    
elif income <= RATE_3_LIMIT:
    incomeTax = RATE_1 * RATE_1_LIMIT + RATE_2 * (RATE_2_LIMIT - RATE_1_LIMIT) + RATE_3 * (income - RATE_2_LIMIT)
    
elif income <= RATE_4_LIMIT:
    incomeTax = RATE_1 * RATE_1_LIMIT + RATE_2 * (RATE_2_LIMIT - RATE_1_LIMIT) + RATE_3 * (RATE_3_LIMIT - RATE_2_LIMIT) + RATE_4 * (income - RATE_3_LIMIT)
    
elif income <= RATE_5_LIMIT:
    incomeTax = RATE_1 * RATE_1_LIMIT + RATE_2 * (RATE_2_LIMIT - RATE_1_LIMIT) + RATE_3 * (RATE_3_LIMIT - RATE_2_LIMIT) + RATE_4 * (RATE_4_LIMIT - RATE_3_LIMIT) + RATE_5 * (income - RATE_4_LIMIT)
    
else:
   if income > RATE_5_LIMIT : 
    incomeTax = RATE_1 * RATE_1_LIMIT + RATE_2 * (RATE_2_LIMIT - RATE_1_LIMIT) + RATE_3 * (RATE_3_LIMIT - RATE_2_LIMIT) + RATE_4 * (RATE_4_LIMIT - RATE_3_LIMIT) + RATE_5 * (RATE_5_LIMIT - RATE_4_LIMIT) + RATE_6 * (income - RATE_5_LIMIT)

print("Income Tax Due: %.2f" % incomeTax)


