#rock paper scissors
import random

results = ["You won!", "You Lost!", "Tie!"]

rps = [0,1,2]

hand = input(("Choose: Rock, Paper, or Scissors: "))

def process():
    oppHand=random.choice(rps)
    print("1,2,3!!")
        


    if hand =="Rock" and oppHand ==0: #rock vs rock
        print("Opponent: Rock" +"-"+results[2]) #tie!
    elif hand == "Rock" and oppHand ==1: #rock vs paper
        print("Opponent: Paper"+"-"+results[1]) #lost
    elif hand =="Rock" and oppHand ==2: #rock vs scissors
        print("Opponent: Scissors"+"-"+ results[0]) #won
    elif hand =="Paper" and oppHand ==0: #paper vs rock
        print("Opponent: Rock"+"-"+ results[0]) #won
    elif hand =="Paper" and oppHand ==1: #paper vs paper
        print("Opponent: Paper"+"-"+ results[2])  #tie!
    elif hand =="Paper" and oppHand ==2: #paper vs scissors
        print("Opponent: Scissors"+"-"+ results[1]) #lost
    elif hand == "Scissors" and oppHand ==0: #scissors vs rock
        print("Opponent: Rock"+"-"+ results[1]) #lost
    elif hand == "Scissors" and oppHand ==1: #scissors vs paper
        print("Opponent: Paper"+"-"+ results[0]) #won
    elif hand =="Scissors" and oppHand ==2: #scissors vs scissors
        print("Opponent: Scissors"+"-"+ results[2]) #tie!
    else: print("Type Rock, Paper, or Scissors")            

   
       
process() 

