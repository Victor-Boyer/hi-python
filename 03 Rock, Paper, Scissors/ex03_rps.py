import sys
import random

def check(input) : 
    if input == 1 :
        return "rock"
    elif input == 2 :
        return "paper"
    elif input == 3 :
        return "scissors"
    else : return "error"

guessed = False    
print("Let's play Rock Paper Scissors !")
while guessed == False :
    UInput = int(input("Press : 1 for Rock ; 2 for Paper ; 3 for Scissors = "))
    userInput = check(UInput)
    botInput = check(random.randrange(1, 4))
    print("You choose : " + str(userInput))
    print("IA choose : " + str(botInput))
    if userInput == botInput : 
        print("No winner, equality !")
    elif userInput == "rock" and botInput == "paper" :
        print("You loose...")
    elif userInput == "rock" and botInput == "scissors" :
        print("Congrat ! You won the game")
    elif userInput == "paper" and botInput == "rock" :
        print("Congrat ! You won the game")
    elif userInput == "paper" and botInput == "scissors" :
        print("You loose...")
    elif userInput == "scissors" and botInput == "rock" :
        print("Youse loose...")
    elif userInput == "scissors" and botInput == "paper" :
        print("Congrat ! You won the game")
    guessed = True;

