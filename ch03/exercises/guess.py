import random
from random import randint

num_guesses = 0
guess_count = 2
radnum = int(randint(1,10))
guess_num = int(input("guess a number: "))

for i in range(guess_count):
  if num_guesses == 3:
      break
  if guess_num != radnum:
    guess_num = int(input("guess a number: "))
    num_guesses += 1
    if guess_num > radnum:
      print("your guess is too high")
    elif guess_num < radnum:
      print("your guess is too low")
  else:
    print("Correct!")
    print("It took you", num_guesses, "to get it right.")
    break