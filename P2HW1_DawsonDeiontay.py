# Deiontay Dawson
# 22 June 2025
# P2HW1_DawsonDeiontay
# Edit and Enhance exiting programs

#Remove lines of code that become redundant. Input function works well to clean code for variable input 
print("This program calculates and displays travel expenses")
print()
budget=float(input("Enter Budget: "))
print()
location=input("Enter your travel destination: ")
print()
gas=float(input("How much do you think you will spend on gas? "))
print()
print("Approximately, how much will you need for accomodation/hotel?", end="")
hotels=int(input())
print()
print("Last, how much do you need for food?", end="")
food=int(input())
print()
print("------------Travel Expenses----------")
print(f"Location:",location)
print(f"Initial Budget:", budget)
print()
print(f"Fuel:", gas)
print(f"Accomodation:", hotels)
print(f"Food:", food)
print()
leftover=float(budget-gas-food-hotels)
print(f"Remaining Balance: {leftover:,.2f}")

# program Pseudocode (logic)
