#Deiontay Dawson
#21 June 2025
#P2LAB2_DawsonDeiontay
#Use a dictionary to store user input and display output

#Create dictionary
car_mpg = {
    'Camaro':18.21, 
    'Prius':52.36,
    'Model S':110, 
    'Silverado':26
}
#Pull Dictionary Keys (variable = dictioanry.keys end parenthesis)
fuel = car_mpg.keys()
print(fuel)

#Create Variable from Dictionary to input
model = input("Enter a vehicle to see it's mpg: ") #User input *if the keys values are printed they know what options are available
eco = car_mpg[model] #Will input the value based upon the keys

#Print statements using f-string using curly bracket to input variables 
print(f"The {model} gets {eco} mpg.")
mileage = float(input(f"How many miles will you drive the {model}?"))
gallons = (mileage/eco) #Use math to create final variable 
print (f"{gallons:.2f} gallon(s) of gas are need to drive the {model} {mileage} miles")