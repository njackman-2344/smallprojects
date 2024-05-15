#Get Away - A text Adventure Game
import random


def story_setup():
  print("You are the getaway driver for 3 others at a Bank.")
  print(
      "All has been going according to plan but plans sometimes have to be flexible."
  )
  print("Choose wisely...Driver")

  print("The 4 of you arrive at the bank in a black Dodge Charger.")
  print(
      "It's fast and loud and gets the attention of the surrounding pedestrians."
  )
  print(
      "The 3 push the Charger's doors, fast walk to their positions. Carrying their gear."
  )


def first_choice():
  print("You notice an old man waiting for the crosswalk looking at you.")
  ch1 = input("Do you stay idle in front or get to the back? Idle or Back: ")
  #choice 1 loop
  dice_roll = random.randint(1, 2)

  if ch1 == "Idle":
    if dice_roll == 1:
      print("The ALARM goes off and you see the 3 sprint towards you.")
      print("You unlock the doors and they jump in. 'Go! Go! Go!' ")
      print("The tires peel off as you enter into the street.")
    else:
      print("The crew runs out and looks around. They can't find you.")
  elif ch1 == "Back":
    if dice_roll == 1:
      print("The ALARM goes off and you see the 3 sprint out.")
      print("You race over and they jump in. 'Go! Go! Go!' ")
      print("The old man watches from bench as you enter the street.")
    else:
      print(
          "Your tire gets a nail in the parking lot and a police car hits you out of nowhere."
      )
  else:
    print("please input word with capital letter. START OVER")


#Tallied for the crimes you've done at the end.
def second():
  print("You escape but your picture is released.")

def punishment():
  print(
      "Red and Blue lights come out of nowhere and fixate on you and your crew"
  )
  print(" LATER....There you are, posing for your mugshot")
  dice_roll = random.randint(1, 1000)
  total_damage = str(f'${dice_roll * 100000}')
  sentence = dice_roll * 9
  print(
      f"You're a menace to society with {total_damage} in damage incurred and to be held behind bars for {sentence} years"
  )


def story_flow():
  story_setup()
  first_choice()
  if first_choice == 1:
    second()
  else:
    punishment()


story_flow()
