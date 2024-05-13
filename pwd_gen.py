#Password Generator
import random

print("Password Generator")
user_input = int(input("How many digits will you use? 5- 12: "))
if user_input < 5:
  print("please try again")
elif user_input > 12:
  print("Too large")
else:
  print("Here is your password")

alphabet = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o",
    "p", "q", "t", "u", "v", "w", "x", "y", "z"
]

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ["!", '*', "$", "#", "@", "&", "^"]

password = alphabet[random.randint(1, 25) + numbers[random.randint(1, 9)] +
                    symbols[random.randint(1, 6)]]
for item in range(1, 5):
  print(password)
