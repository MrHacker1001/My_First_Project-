import random

from numpy import number

computer = random.choice([0, 1, 2])
print(computer)
you = input("Enter 0 for rock, 1 for paper, and 2 for scissors: ")
youDictionary = {0: "rock", 1: "paper", 2: "scissors"}
you = int(you)
reverseDictionary = {0: "rock", 1: "paper", 2: "scissors"}
print ("Computer chose: " + reverseDictionary[computer])
print ("You chose: " + youDictionary[you])
if(you >= computer):
    print ("you gain 10 points")
elif(you == computer):
    print ("you gain 5 points")
else:
    print ("you lose 10 points")
if (computer == you ):
    print ("Draw")
else:
    if(computer == 0 and you ==1):
        print ("You win")
    elif(computer == 0 and you == 2):
        print ("You lose")
    elif(computer == 1 and you == 0):
        print ("You lose")
    elif(computer == 1 and you == 2):
        print ("You win")
    elif(computer == 2 and you == 0):
        print ("You win")
    elif(computer == 2 and you == 1):
        print ("You lose")
    else:
        print ("Invalid input")