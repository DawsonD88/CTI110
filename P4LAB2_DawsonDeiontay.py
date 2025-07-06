#Deiontay Dawson
#6 July 2025
#P4LAB1_DawsonDeiontay
#Testing while and for loops in program

#Get input from user
start = 'yes'

while start != "no":
#Create while loop that user input does not equal no

    num=int(input("Enter an integer: "))
#If input is positve display Multiplication table
    print()
    if num >= 0:
            for item in range(1,13):
                print(f"{num} * {item} = {num * item}")
    else:
        print(f"\nThis program does not handle negative numbers")

    start = input(f"\nWould you like to run again? ")

#Broke the loop after user said 'No"
print(f"\nExiting program...")
