#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tues Feb 20 12:56:28 2024

@author: eschuler
"""

# Original code up to the creation of the incomes dictionary
incomes = {}
inf = open("rawdata_2004.txt", "r")

for line in inf:
    parts = line.split("\t")
    parts[2] = parts[2].replace("$", "")
    parts[2] = parts[2].replace(",", "")
    incomes[parts[1].upper()] = float(parts[2])

inf.close()

# Creating the new dictionary (letters) with countries starting with each letter
letters = {}
for country in incomes.keys():
    first_letter = country[0]
    if first_letter not in letters:
        letters[first_letter] = set()
    letters[first_letter].add(country)

# Read queries from the user and respond to them.
country = input("Enter a country name (or type quit to quit): ").upper()

while country != "QUIT":
    if len(country) == 1:
        if country in letters:
            print("Countries starting with", country + ":")
            for country_name in sorted(letters[country]):
                print(country_name)
        else:
            print("No countries starting with", country)
    else:
        if country in incomes:
            print("The per capita income is", incomes[country])
        else:
            print("The text entered is not a recognized country.")

    print()
    country = input("Enter a country name (or type quit to quit): ").upper()

