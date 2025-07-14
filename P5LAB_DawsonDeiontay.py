#Deiontay Dawson
#14 July 2025
#P5LAB_DawsonDeiontay
#Self-Checkout Machine 

import random
    #Import random
def disperse_change(change):
    #Input variable from user then convert to integer
    change = round(change * 100)

    #Breakdown of money count
    num_dollars = change // 100
    change = change - (num_dollars * 100)

    num_quarters = change // 25
    change = change - (num_quarters * 25)

    num_dimes = change // 10
    change = change - (num_dimes * 10)

    num_nickels = change // 5
    change = change - (num_nickels * 5)

    num_pennies = change

    #If/Else statements plural for multiples and singular for singles

    if num_dollars > 0:
        if num_dollars == 1:
            print(f"{num_dollars} Dollar")
        else:
            print(f"{num_dollars} Dollars")

    if num_quarters > 0:
        if num_quarters == 1:
            print(f"{num_quarters} Quarter")
        else:
            print(f"{num_quarters} Quarters")

    if num_dimes > 0:
        if num_dimes == 1:
            print(f"{num_dimes} Dime")
        else:
            print(f"{num_dimes} Dimes")

    if num_nickels > 0:
        if num_nickels == 1:
            print(f"{num_nickels} Nickel")
        else:
            print(f"{num_nickels} Nickels")

    if num_pennies > 0:
        if num_pennies == 1:
            print(f"{num_pennies} Penny")
        else:
            print(f"{num_pennies} Pennies")
    else:
        print(f"No change")

def main():
    #Define main then generate the function, Ensure to call 'main()'

    #Money owed
    owed=round(random.uniform(0.01, 100.00), 2)
    print(f"You owe: ${owed:.2f}")

    #Cash in
    cash=float(input(f"How much cash will you put in the self-checkout? "))

    #Calculate change
    change=cash - owed
    print(f"Change is: ${change:.2f}\n")

    #Call disperse_change function
    disperse_change(change)

main()    
