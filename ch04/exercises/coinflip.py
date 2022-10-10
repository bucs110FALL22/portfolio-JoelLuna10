import random
import turtle

koopa = turtle.Turtle()
wn = turtle.Screen()
koopa.shape("turtle")
koopa.speed(4)

distance = 10
angle = 90
is_in_screen = True
wn = turtle.Screen() 

while is_in_screen:
  coin = random.randrange(0,2)
  if coin == 0:
    koopa.left(angle)
  else:
    koopa.right(angle)
    
  koopa.forward(distance)
  turtleX = koopa.xcor()
  turtleY = koopa.ycor()
  x_range = wn.window_width()/2
  y_range = wn.window_height()/2
  koopa.color("Green")
  
  if abs(turtleX)> x_range or abs(turtleY) > y_range:
    is_in_screen = False

wn.bgcolor("black")
wn.exitonclick()

