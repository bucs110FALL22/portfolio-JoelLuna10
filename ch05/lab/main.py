import pygame
import math

count = 0
display = pygame.display.set_mode()
#PartA:
n = int(input("Enter a number: "))
upper_limit = 20
iters = {}

def sequence(n, count, iters):
  while n != 1.0:
    count += 1
    if n%2 == 0.0 and n != 1.0:
      n = (n/2)
      print(n)
    elif n%2 == 1.0 and n != 1.0:
      n = (n*3.0) + 1.0
      print(n)
    elif n == 1.0:
      print("This took", count, "attempts.")
      pygame.quit()
    n = iters
    iters.items()

sequence(n)

#PartBT)TTHT HTEJHT
