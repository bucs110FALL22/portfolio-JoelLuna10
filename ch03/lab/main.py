import turtle  #1. import modules
import random
import pygame
import math

#Part A
window = turtle.Screen()  # 2.  Create a screen
window.bgcolor('lightblue')

finishline = 200
move = random.randrange(0, 11)
max = 11

michelangelo = turtle.Turtle()  # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()  # 4. Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)

## 5. Your PART A code goes here

leonardo.forward(move)
michelangelo.forward(move)
michelangelo.goto(-100, 20)
leonardo.goto(-100, -20)

for race in range(max):
    if race < (max - 1):
        leonardo.forward(move)
        michelangelo.forward(move)
    elif race > (max - 2):
        michelangelo.goto(-100, 20)
        leonardo.goto(-100, -20)
      
window.exitonclick()

# PART B - complete part B here
pygame.init()
window = pygame.display.set_mode()
side_length = 25
offset = pygame.display.get_window_size()[1]/4
inputs = [1,2,3,4,5]

for s in inputs:
  points = []
  points2 = []
  points3 = []
  points4 = []
  points5 = []
  num_sides = int(input("Type # of sides: "))
  for shape in range(num_sides):
    theta = (2.0 * math.pi * (shape)) / num_sides
    x = side_length * math.cos(theta) + offset
    y = side_length * math.sin(theta) + offset
    x1 = (side_length * math.cos(theta) + offset)+50
    y1 = (side_length * math.sin(theta) + offset)
    x2 = (side_length * math.cos(theta) + offset)+100
    y2 = (side_length * math.sin(theta) + offset)
    points.append([x,y])
    points2.append([x1,y1])
    points3.append([x2,y2])

  pygame.draw.polygon(window, "green", points)
  pygame.draw.polygon(window, "green", points2)
  pygame.draw.polygon(window, "green", points3)
  pygame.time.wait(400)
  pygame.display.flip()
  window.fill("black")
  pygame.time.wait(400)