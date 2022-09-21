import random

num_guesses = 1

correct_guess = false

for i in range(5):
  if not correct_guess:
    guess_num = int(input("Please enter a quess:"))
  num_guesses += 1
  if guess_num > num:
    print("your guess is too high")
  elif guess_name < num:
    print("your guess is too low")
  else:
    print("Correct!")
    break

print("It took you", num_quesses, "to get it right.")