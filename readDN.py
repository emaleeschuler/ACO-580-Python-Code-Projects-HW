#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 12:05:23 2024

@author: eschuler
"""

##
# Use a function to read a floating point value from the user.
#
def main() :
    salary = readFloat("please enter your salary: ")
    percentageRaise = readFloat("What percentage raise would you like?: ")
    print("The salary is", salary)
    print("The raise percentage is", percentageRaise)
    
## Read a floating point number from the user.
# @param prompt the promtp to display for the user
# @return the number entered by the user as a floating point value
#
def readFloat(prompt) :
    user_input = input(prompt)
# Check if input can be converted to a float
    if user_input.replace('.', '', 1).isdigit():  
        # Check if input can be converted to a float
        return float(user_input)
    else:
        print("Invalid input. Please enter a valid floating-point number.")
        return readFloat(prompt)
# Call the main function.
main()


