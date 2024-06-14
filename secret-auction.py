#secret auction

print("Welcome to the secret auction program.")


def auction1():
  dict_bid = {}
  name1 = input("What is your name?: ")
  bid1 = int(input("what is your bid?: "))
  dict_bid[name1] = bid1
  bidder1 = input("Is there another bidder (y/n): ")

  if bidder1 == "y":
    name2 = input("What is your name?: ")
    bid2 = int(input("what is your bid?: "))
    dict_bid[name2] = bid2
  else:
    print(f"Thank you and {name1} won")
    quit()

  
  bidder2 = input("Is there another bidder (y/n): ")


  if bidder2 == "y":
    name3 = input("What is your name?: ")
    bid3 = int(input("what is your bid?: "))
    dict_bid[name3] = bid3
    print(dict_bid)
    if dict_bid[name3] > dict_bid[name2] and dict_bid[name3] > dict_bid[name1]:
      print(f"{name3} won!")
    elif dict_bid[name1] > dict_bid[name2] and dict_bid[name1] > dict_bid[
        name2]:
      print(f" {name1} won!")
    elif dict_bid[name2] > dict_bid[name1] and dict_bid[name2] > dict_bid[
        name3]:
      print(f" {name2} won!")
    else:
      print("Tie! Try again")
  elif dict_bid[name1] > dict_bid[name2]:
      print(f"{name1} won")
  else:
      print(f"{name2} won")



auction1()
