import turtle

window = turtle.Screen()
koopa = turtle.Turtle()
koopa.shape("turtle")
koopa.color("purple")

side = 50
length = 50

for m in range(length): 
  koopa.forward(side)
  koopa.right(90)
  koopa.forward(side)
  koopa.right(90)
  koopa.forward(side)
  koopa.right(90)
  koopa.forward(side)
  koopa.right(90)
  side = side - 1
  if side < (side+1):
    koopa.left(90)

window.exitonclick()

