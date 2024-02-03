import sys
import random
from enum import Enum

game_count = 0


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

            def decide_winner(playerChoice, computerChoice):
                if playerChoice == computerChoice:
                    return "It's a tie!"
                elif playerChoice == 1 and computerChoice == 3:
                    return "You win!"
                elif playerChoice == 2 and computerChoice == 1:
                    return "You win!"
                elif playerChoice == 3 and computerChoice == 2:
                    return "You win!"
                else:
                    return "Python wins!"

            game_result = decide_winner(playerChoice, computerChoice)
            print(game_result)

            global game_count
            game_count += 1

            print("\nGame Count: " + str(game_count))

            play_again = input("\nPlay again? \nY for Yes or \nQ to Quit\n")

            if play_again.lower() == "y":
                continue
            elif play_again.lower() == "q":
                print("\nThank you for playing!\n")
                sys.exit("Bye!")
            else:
                print("Invalid input. Please enter 'Y' or 'Q'.")
                break  # * Exit the loop if an invalid input is provided.

        except ValueError:
            print("Invalid input. Please enter a number (1, 2, or 3).")


play_rps()
