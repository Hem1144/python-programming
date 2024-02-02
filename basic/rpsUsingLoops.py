import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


playagain = True

while playagain:

    # print(RPS(2))
    # print(RPS.ROCK)
    # print(RPS["ROCK"])
    # print(RPS.ROCK.value)
    # sys.exit()

    playerChoice = input(
        "\nEnter...\n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n"
    )

    player = int(playerChoice)

    if player < 1 | player > 3:
        sys.exit("You must enter 1,2 or 3.")

    computerChoice = random.choice("123")

    computer = int(computerChoice)
    print("\nYour chose " + str(RPS(player)).replace("RPS.", "") + ".")
    print("Python chose " + str(RPS(computer)).replace("RPS.", "") + ".\n")

    if player == 1 and computer == 3:
        print("You wins!")
    elif player == 2 and computer == 1:
        print("You wins!")
    elif player == 3 and computer == 2:
        print("You wins!")
    elif player == computer:
        print("Tie again!")
    else:
        print("Python wins!")

    playagain = input("\nPlay again? \nY for Yes or \nQ to Quit \n\n ")

    if (playagain.lower()) == "y":
        continue
    else:
        print("\nCelebrate ")
        print("Thank you for playing!\n")
        playagain = False

sys.exit("Bye!")
