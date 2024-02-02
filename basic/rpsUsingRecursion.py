import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


def play_rps():
    while True:
        try:
            playerChoice = int(
                input("\nEnter...\n1 for Rock, \n2 for Paper, or \n3 for Scissors:\n\n")
            )

            if playerChoice not in [1, 2, 3]:
                print("You must enter 1, 2, or 3.")
                continue

            computerChoice = random.randint(1, 3)

            print("\nYou chose " + str(RPS(playerChoice)).split(".")[1] + ".")
            print("Python chose " + str(RPS(computerChoice)).split(".")[1] + ".\n")

            if playerChoice == 1 and computerChoice == 3:
                print("You win!")
            elif playerChoice == 2 and computerChoice == 1:
                print("You win!")
            elif playerChoice == 3 and computerChoice == 2:
                print("You win!")
            elif playerChoice == computerChoice:
                print("It's a tie!")
            else:
                print("Python wins!")

            play_again = input("\nPlay again? \nY for Yes or \nQ to Quit\n")

            if play_again.lower() == "y":
                continue
            elif play_again.lower() == "q":
                print("\nThank you for playing!\n")
                sys.exit("Bye!")
            else:
                print("Invalid input. Please enter 'Y' or 'Q'.")
                continue

        except ValueError:
            print("Invalid input. Please enter a number (1, 2, or 3).")


if __name__ == "__main__":
    play_rps()
