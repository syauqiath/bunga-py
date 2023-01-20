import turtle

turtle.bgcolor("grey")
turtle.speed(0)
turtle.hideturtle()

Colors = ["white", "yellow", "white", "yellow"]
# Colors = ["yellow", "yellow", "black", "yellow"]

for i in range(120):
    for c in Colors:
        turtle.color(c)
        turtle.circle(200-i, 100)
        turtle.lt(90)
        turtle.circle(200-i, 100)
        turtle.rt(60)
        turtle.end_fill()

turtle.mainloop()
