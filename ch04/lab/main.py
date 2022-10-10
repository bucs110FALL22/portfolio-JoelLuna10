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
game = 0
p1pts = 0
p2pts = 0
wait = 1000
buttonP1 = pygame.draw.rect(window, "blue", pygame.Rect(0, 0, 50, 50))
buttonP2 = pygame.draw.rect(window, "green", pygame.Rect(350, 0, 50, 50))
pygame.display.flip()

#Part B
print("Pick a color you think will win")
while game == 0:
  rounds = 10
  for event in pygame.event.get():
    if event.type == pygame.MOUSEBUTTONDOWN:
      pos = pygame.mouse.get_pos()
      if buttonP1.collidepoint(pos):
        print("Player choose blue")
        game = 1
      if buttonP2.collidepoint(pos):
        print("Player choose green")
        game = 2
  if game == 1:
    for i in range(rounds):
      print("Round ", i+1)
      randx1 = random.randint(0,400)
      randy1 = random.randint(0,400)
      distance_from_center = math.hypot(200-randx1, 125-randy1)
      is_in_circle = distance_from_center <= 200/2 
      is_out_circle = distance_from_center > 200/2 
      randx2 = random.randint(0,400)
      randy2 = random.randint(0,400)
      distance_from_center2 = math.hypot(200-randx2, 125-randy2)
      is_in_circle2 = distance_from_center2 <= 200/2 
      is_out_circle2 = distance_from_center2 > 200/2 
      if is_in_circle:
        p1pts += 1
        print("Blue pts: ", p1pts)
        pygame.draw.circle(window, "blue", (randx1,randy1), 5)
        pygame.time.wait(wait)
        pygame.display.flip()
      if is_in_circle2:
        p2pts += 1
        print("Green pts: ", p2pts)
        pygame.draw.circle(window, "green", (randx2,randy2), 5)
        pygame.time.wait(wait)
        pygame.display.flip()
      if is_out_circle:
        print("Blue pts: ", p1pts)
        pygame.draw.circle(window, "lightblue", (randx1,randy1), 5)
        pygame.time.wait(wait)
        pygame.display.flip()
      if is_out_circle2:
        print("Green pts: ", p2pts)
        pygame.draw.circle(window, "lightgreen", (randx2,randy2), 5)
        pygame.time.wait(wait)
        pygame.display.flip()
           
    if p1pts > p2pts:
      print("You Won")
      game = 3
    if p1pts == p2pts:
      print("Tie")
      game = 3
    if p1pts < p2pts:
      print("You Lost")
      game = 3
      
  if game == 2:
    for i in range(rounds):
      print("Round ", i+1)
      randx1 = random.randint(0,400)
      randy1 = random.randint(0,400)
      distance_from_center = math.hypot(200-randx1, 125-randy1)
      is_in_circle = distance_from_center <= 200/2 
      is_out_circle = distance_from_center > 200/2 
      randx2 = random.randint(0,400)
      randy2 = random.randint(0,400)
      distance_from_center2 = math.hypot(200-randx2, 125-randy2)
      is_in_circle2 = distance_from_center2 <= 200/2 
      is_out_circle2 = distance_from_center2 > 200/2 
      if is_in_circle:
        p1pts += 1
        print("Blue pts: ", p1pts)
        pygame.draw.circle(window, "blue", (randx1,randy1), 5)
        pygame.time.wait(wait)
        pygame.display.flip()
      if is_in_circle2:
        p2pts += 1
        print("Green pts: ", p2pts)
        pygame.draw.circle(window, "green", (randx2,randy2), 5)
        pygame.time.wait(wait)
        pygame.display.flip()
      if is_out_circle:
        print("Blue pts: ", p1pts)
        pygame.draw.circle(window, "lightblue", (randx1,randy1), 5)
        pygame.time.wait(wait)
        pygame.display.flip()
      if is_out_circle2:
        print("Green pts: ", p2pts)
        pygame.draw.circle(window, "lightgreen", (randx2,randy2), 5)
        pygame.time.wait(wait)
        pygame.display.flip()
           
    if p2pts > p1pts:
      print("You Won")
      game = 3
    if p2pts == p1pts:
      print("Tie")
      game = 3
    if p2pts < p1pts:
      print("You Lost")
      game = 3
    
if game == 3:
  pygame.quit()

      


      
    
    







