#Deiontay Dawson
#7 July 2025
#P2HW2_DawsonDeiontay
#Program for Employee Pay Data

#This program was written in psuedocode
#Initialize Counters
employee = 0
total_over = 0
total_reg = 0
total_gross = 0

#Enter Employee Information, start loop
while True:
    employees = input("Enter employee's name or \"Done\" to terminate: ")

    if employees == "Done":
        break
    
    hours = float(input(f"How many hours did {employees} work? "))
    pay = float(input(f"What is {employees}'s pay rate? "))
    print(f"\nEmployee Name:    {employees}")

    over = 0
            
    #Create strings for input allowing for numbers to adjust with inputted data
    if hours > 40: #If equals 40 the just calculate regular pay
        over = float(int(hours - 40))
        regpay = float(pay * 40)
        overpay = float((pay*1.5) * over)
        gross = overpay + regpay
        pay = regpay
         
    else:
        regpay = float(pay * hours)
        overpay = 0
        gross = regpay

    employee += 1
    total_over += overpay
    total_reg += regpay
    total_gross += gross

    print(f"\nHours Worked    Pay Rate    Overtime    OverTime Pay     RegHour Pay     Gross Pay") #Insert newline and format spacing for headers
    print("----------------------------------------------------------------------------------------")
    print(f"{hours:.1f} {pay:>15.1f} {over:>10.1f} {overpay:>14,.2f}           ${regpay:,.2f}        ${gross:,.2f}\n\n")    

print(f"\nTotal number of employees entered: {employee}")
print(f"Total amount paid for overtime: ${total_over}")
print(f"Total amount paid for regular hours: ${total_reg}")
print(f"Total amount paid in gross: ${total_gross}")

