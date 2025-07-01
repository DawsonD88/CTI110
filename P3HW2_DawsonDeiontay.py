#Deiontay Dawson
#29 June 2025
#P2HW2_DawsonDeiontay
#Program for Employee Pay Data

#This program was written in psuedocode

#Enter Employee Information
employee = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked: "))
pay = float(input("Enter employee's pay rate: "))
over = float(int(hours - 40))
regpay = float(pay * 40)
overpay = float((pay*1.5) * over)
gross = overpay + regpay
print("---------------------------------")
print(f"Employee Name:   {employee}")
print(f"\nHours Worked    Pay Rate    Overtime    OverTime Pay     RegHour Pay     Gross Pay") #Insert newline and format spacing for headers
print("----------------------------------------------------------------------------------------")
#Create strings for input allowing for numbers to adjust with inputted data
if hours == 40: #If equals 40 the just calculate regular pay
    pay = regpay
    print(f'{hours:.1f} {pay:>15.1f} {over:>10.1f} {overpay:>14,.2f} {regpay:>16,.2f} {gross:>15,.2f}') 
elif hours  >= 40: #else if over 40 calculate the overtime pay
    overpay = overpay
    print(f"{hours:.1f} {pay:>15.1f} {over:>10.1f} {overpay:>14,.2f} {regpay:>16,.2f} {gross:>15,.2f}")
else:
    print(f"{hours:.1f} {pay:>15.1f} {over:>10.1f} {overpay:>14,.2f} {regpay:>16,.2f} {gross:>15,.2f}")
