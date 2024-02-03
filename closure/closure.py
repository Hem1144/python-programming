def parent_function(person, coins):
    # coins = 3

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " has " + str(coins) + " coins left.")
        else:
            print("\n" + person + " is out of coins.")

    return play_game


demo = parent_function("Demo", 3)
root = parent_function("Root", 5)

root()
root()

demo()
demo()
