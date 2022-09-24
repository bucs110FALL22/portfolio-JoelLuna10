import turtle

koopa = turtle.Turtle()
koopa.shape("turtle")
window = turtle.Screen()

side = int(input("Type # of side(s)"))
length = int(input("Type # of length(s)"))

for m in range(4):
  koopa.forward(side)
  koopa.right(90)
  koopa.forward(length)
  koopa.right(90)
window.exitonclick()