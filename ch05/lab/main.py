import pygame
import math


#PartA:
n = int(input("Enter a number: "))
upper_limit = 20
iters = {}

def sequence(n):
  count = 0
  while n != 1.0:
    count += 1
    if n%2 == 0.0 and n != 1.0:
      n = (n/2)
      print(n)
    if n%2 == 1.0 and n != 1.0:
      n = (n*3.0) + 1.0
      print(n)
    elif n == 1.0:
      print("This took", count, "attempts.")
      pygame.quit()

sequence(n)

#PartBT)TTHT HTEJHT
