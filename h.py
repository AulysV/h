from turtle import *

shape("turtle")
shapesize(5,5,5)
fillcolor("green")


setup(500, 10)

speed(1)

pensize(15)

penup()
setpos(0, 0)

forward(250)
pendown()
color("red")
begin_fill()
left(90)
circle(250)
end_fill()

penup()
setpos(0, 0)

forward(200)
pendown()
color("white")
begin_fill()
left(90)
circle(200)
end_fill()


left(45)

setpos(0, 0)

color("black")
pensize(20)

for i in range(4):
    pendown()
    forward(100)
    left(-90)
    forward(100)
    penup()
    setpos(0, 0)

exitonclick()

