import random


# 1. Display an intro/welcome message to the player.
# 2. Store a random number as the answer/solution.
# 3. Continuously prompt the player for a guess.
#   a. If the guess greater than the solution, display to the player "It's lower".
#   b. If the guess is less than the solution, display to the player "It's higher".

# 4. Once the guess is correct, stop looping, inform the user they "Got it"
#      and show how many attempts it took them to get the correct number.
# 5. Let the player know the game is ending, or something that indicates the game is over.


def start_game():
    print("""
    ._______________________.
    |_____Welcome to my_____|
    |_Number Guessing Game!_|
    |_______________________|""")
    random_num = random.randint(1, 25)
    guesses = []
    player_guess = int(input("Guess a number between 1 and 25:  "))
    while player_guess != random_num:
        player_guess = int(input("Incorrect! Try again...  "))


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
