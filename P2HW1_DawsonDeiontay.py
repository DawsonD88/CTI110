# Deiontay Dawson
# 22 June 2025
# P2HW1_DawsonDeiontay
# Edit and Enhance exiting programs
 
print(f"\nThis program calculates and displays travel expenses")
budget=float(input(f"\nEnter Budget: ")) 
location=input(f"\nEnter your travel destination: ")
gas=float(input(f"\nHow much do you think you will spend on gas? "))
hotels=float(input(f"\nApproximately, how much will you need for accomodation/hotel? "))
food=float(input(f"\nLast, how much do you need for food? "))
print(f"------------Travel Expenses----------")
print(f"Location:\t\t{location}")
print(f"Initial Budget:\t\t${budget:,.2f}")
print(f"Fuel:\t\t\t${gas:,.2f}")
print(f"Accomodation:\t\t${hotels:,.2f}")
print(f"Food:\t\t\t${food:,.2f}")
print(f"-------------------------------------")
leftover=float(budget-gas-food-hotels)
print(f"\nRemaining Balance:\t${leftover:,.2f}")

# program Pseudocode (logic)
