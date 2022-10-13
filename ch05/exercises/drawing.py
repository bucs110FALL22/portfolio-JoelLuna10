import turtle

wn = turtle.Screen()
koopa = turtle.Turtle()
koopa.shape("turtle")
koopa.color("green")

num_sides = int(input("Type in # of sides:"))
side_lengths = int(input("Type in # of sidelengths:"))


def drawEqShape(num_sides, side_lengths):
  angle = 360
  moveangle = (angle/num_sides)
  for i in range(num_sides):
    koopa.forward(side_lengths)
    koopa.left(moveangle)



drawEqShape(num_sides, side_lengths)
    

    
wn.exitonclick()