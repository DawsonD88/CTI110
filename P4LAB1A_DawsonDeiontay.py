#Deiontay Dawson
#6 July 2025
#P4LAB1_DawsonDeiontay
#Turtle Program (Shapes)

#import and create turtle enivronment
import turtle
win = turtle.Screen()
win.bgcolor("cyan")
ebony = turtle.Turtle()
ebony.shape("turtle")
ebony.color("yellow")

zeus = turtle.Turtle()
zeus.shape("turtle")
zeus.color("red")

#For Loop or While Loop to move the turtle
ebony.penup()
ebony.backward (50)
ebony.pendown()
zeus.pendown()
for x in range(4):
    ebony.stamp() #leave impression
    ebony.left(90) #turn at and angle
    ebony.forward(200) #move forward
for y in range(3):
    zeus.stamp()
    zeus.forward(225)
    zeus.left(120)
#End Command
win.mainloop()
