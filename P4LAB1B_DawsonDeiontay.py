#Deiontay Dawson
#6 July 2025
#P4LAB1_DawsonDeiontay
#Turtle Program (Initials)

#import and create turtle enivronment
import turtle
win = turtle.Screen()
win.bgcolor("cyan")

#turtle attributes
ebony = turtle.Turtle()
ebony.shape("turtle")
ebony.color("yellow")

zeus = turtle.Turtle()
zeus.shape("turtle")
zeus.color("red")

#For Loop to move the turtle
ebony.penup() #enable movement of turtle without drawing line
ebony.backward (200) #move turtle backwards so no on top of other
ebony.pendown() #drop pen to begin drawing
space = 3
ebony.left(90)
ebony.forward(180)
for x in range(13):
    space = space + 4 #create spacing for loop to reach back to beginning
    ebony.forward(space) #move at the variable indicated for space
    ebony.right(21) #each step turn angle at this degree 
zeus.pendown()
space = 3
zeus.left(90)
zeus.forward(180)
for y in range(13):
    space = space + 4
    zeus.forward(space)
    zeus.right(21)
zeus.penup()    
#End Command
win.mainloop()
