import pygame

for event in pygame.event.get():
  if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_w:
        print("Move the character forwards")
    elif event.key == pygame.K_s:
        print("Move the character backwards")
    elif event.key == pygame.K_a:
        print("Move the character left")
    elif event.key == pygame.K_d:
        print("Move the character right")
