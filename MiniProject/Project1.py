## GUESS THE CORRECT NUMBER

import random

Target = random.randint(1,100)
Target  = 40
while True:
    userChoice = input("Guess the number or Quiet(Q): ")

    if(userChoice == "Q"):
        break

    userChoice = int(userChoice)
    if(userChoice == Target):
        print("Sucess: Correct Guess")
        break

    elif(userChoice<Target):
        print("Your Number is too small take a bigger guess")

    elif(userChoice>Target):
        print("Your number is too big take a smaller guess")


print("---GAME OVER---")


