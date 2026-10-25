import random

# how many player in Game
DiceNumber = random.randint(1, 6)
PlayerNumber = int(input("How Many Player Do you want Play"))
# init
TurnCounter = 1
ExitGame = False
ContinueGame = "y"
while not ExitGame:
    # dice play for all players , after finished show do you want exit
    print("Next Player Turn:Player", TurnCounter)
    DiceNumber = random.randint(1, 6)
    print("Dice Number :", DiceNumber)
    if DiceNumber == 6:
        print("you Have another chance")
        DiceNumber = random.randint(1, 6)
        print("Your Lucky Dice Number :", DiceNumber)

        while DiceNumber == 6:
            print("you Have another chance")
            print("Your Lucky Dice Number :", DiceNumber)

            DiceNumber = random.randint(1, 6)

    if TurnCounter == PlayerNumber:
        TurnCounter = 0
        ContinueGame = input("Do you want continue,y or n")
        if ContinueGame == "n":
            ExitGame = True
    TurnCounter += 1
