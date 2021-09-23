import random
import re
from hangman_design import *

wordsList = []
pdv = 9
words = open("RandomFrenchWords.txt", "r")

for line in words.readlines():
    wordsList.append(line[:-1])

randomWord = wordsList[random.randint(0,len(wordsList)-1)].lower()
hidenWord = "_"*len(randomWord)

hangmandesign0()

while hidenWord != randomWord:
    response = input("Propose a letter : ")
    while len(response) > 1 or len(re.findall("([0-9]+)", response)) > 0 :
        response= input("Propose a single letter : ")

    positions = []
    for m in re.finditer(response, randomWord):
        positions.append(m.start())

    if len(positions) < 1:
        pdv-=1
        hangmandesign(pdv)
        if pdv == 0 :
            print("YOU LOOSE")
            break
        print("NOPE")
        print(hidenWord)
    else:   
        for i in positions:
            hidenWord=hidenWord[0:i]+response+hidenWord[i+1:]
        print("MATCH")
        print(hidenWord)

if pdv > 0 :
    print("YOU WIN")