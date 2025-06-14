# Deiontay Dawson
# 14 June 2025
# P1HW2_DawsonDeiontay
# Using IDLE to create and test a program for calculating expenses

print("This program calculates and displays travel expenses")
print()
print("Enter Budget:", end="")
budget=int(input())
print()
print("Enter your travel destination:", end="")
location=input()
print()
print("How much do you think you will spend on gas?", end="")
gas=int(input())
print()
print("Approximately, how much will you need for accomodation/hotel?", end="")
hotels=int(input())
print()
print("Last, how much do you need for food?", end="")
food=int(input())
print()
print("------------Travel Expenses----------")
print("Location:",location)
print("Initial Budget:", budget)
print()
print("Fuel:", gas)
print("Accomodation:", hotels)
print("Food:", food)
print()
leftover=int(budget-gas-food-hotels)
print("Remaining Balance:", leftover)

# program Pseudocode (logic)
