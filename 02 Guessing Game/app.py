import sys
import random

if len(sys.argv) > 2 :
    min = int(sys.argv[1])
    max = int(sys.argv[2])
    if max > min :
        answer = random.randrange(min, max)
        guessed = False    
        print('Guess a number between '+ str(min) +' and '+ str(max))
        while guessed == False :
            userInput = int(input("Please enter your guess: "))
            if userInput < answer : 
                print("Your guess is too small")
            elif userInput > answer :
                print("Your guess is too large")
            elif userInput == answer :
                print("Congrat ! You won the game")
                guessed = True
    else : print("Max must be bigger than min")
else : print("Please put 2 arguments")