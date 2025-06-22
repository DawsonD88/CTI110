#Deiontay Dawson
#21 June 2025
#P2LAB1_DawsonDeiontay
#Perform mathematical calculations and display information

# Circle Formulas
#import math functions
import math

#input your formulas *float() is for decimals/int() is for whole numbers
pi = math.pi
radius = float(input("What is the radius of the circle?"))
print()

diameter = 2 * radius
d = float(f"{diameter:.1f}")
print("The diameter of the circle is", d)
print()

circumference = 2 * pi * radius
c = float(f"{circumference:.2f}")
print("The circumference of the circle is", c)
print()

area = pi * radius**2 #(** is for exponents or use math.sqrt) (**) is better for this due to the equation being pi*radius(squared)
a = float(f"{area:.3f}")
print("The area of the circle is", a)
