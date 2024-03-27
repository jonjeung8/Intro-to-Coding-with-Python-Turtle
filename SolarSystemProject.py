from turtle import *

speed(0)

#set the background color to BLACK
bgcolor("black")

#create the ORANGE planet
color("orange")
begin_fill()
circle(60)
end_fill()

#move forwards
penup()
forward(100)
pendown()

#create the GREY planet
color("grey")
begin_fill()
circle(20)
end_fill()

#move forwards
penup()
forward(100)
pendown()

#create the RED planet
color("red")
begin_fill()
circle(40)
end_fill()

#move forwards
penup()
forward(100)
pendown()

#create the GREEN planet
color("green")
begin_fill()
circle(30)
end_fill()

done()
