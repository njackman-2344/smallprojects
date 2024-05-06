#Number guessing
import random

print("Which player's number is closer?")

player1 = int(input("Player 1, Guess a number between 1 - 10: "))
player2 = int(input("Player 2, Guess another number: "))
num_random = random.randint(1, 10)

step1 = abs(num_random - player1)
step2 = abs(num_random - player2)

if player1 == num_random:
  print(f"Random: {num_random}")
elif step1 < step2:
  print("Player 1 is closer or correct.")
  if num_random < 3 and step1 > step2:
    print("Player 2 is closer.")
  else:
    print(f" Random: {num_random}")
elif player2 == num_random:
  print(f"Random: {num_random}")
elif step1 > step2:
  print(f"Player 2 is closer or correct. Random: {num_random}")
else:
  print(f"Error? {num_random}")

# ISSUE? - in regards to over estimating vs under-estimating