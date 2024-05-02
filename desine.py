import turtle

# Set up the turtle
turtle.speed(0)
turtle.bgcolor("black")
turtle.color("red")
turtle.width(2)

# Draw the rose shape
for _ in range(36):
    turtle.forward(100)
    turtle.left(45)
    turtle.forward(100)
    turtle.left(135)
    turtle.forward(100)
    turtle.left(45)
    turtle.forward(100)
    turtle.left(135)
    turtle.right(10)

# Hide the turtle
turtle.hideturtle()

# Exit on click
turtle.exitonclick()
