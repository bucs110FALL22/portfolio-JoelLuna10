import pygame
import random
import math

#Part A
pygame.init()
window = pygame.display.set_mode((400,400))
window.fill("white")
dartboard = pygame.draw.circle(window, "red", (200,125), 100)
pygame.draw.line(window, "black", (0,125),(400,125),1)
pygame.draw.line(window, "black", (200,0),(200,400),1)

#Part C
p1ptsb = pygame.draw.rect(window, "blue", pygame.Rect(0, 0, 50, 50))
p2ptsb = pygame.draw.rect(window, "green", pygame.Rect(350, 0, 50, 50))

x, y = pygame.mouse.get_pos()
print(x, y)

p1pts = 0
p2pts = 0
pygame.display.flip()



#Part B
for i in range(11):
  randx1 = random.randint(0,400)
  randy1 = random.randint(0,400)
  distance_from_center = math.hypot(200-randx1, 125-randy1)
  is_in_circle = distance_from_center <= 200/2 
  randx2 = random.randint(0,400)
  randy2 = random.randint(0,400)
  distance_from_center2 = math.hypot(200-randx2, 125-randy2)
  is_in_circle2 = distance_from_center2 <= 200/2 
  if is_in_circle:
    pygame.draw.circle(window, "blue", (randx1,randy1), 5)
    pygame.time.wait(400)
    p1pts += 1
    print(p1pts)
    pygame.display.flip()
  else:
    pygame.draw.circle(window, "lightblue", (randx1,randy1), 5)
    pygame.time.wait(400)
    pygame.display.flip()
    
    







