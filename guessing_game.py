import random


# TODO: Create separate "def" for highscore and put the main game within that as to save highscores between games.


def start_game():
    # 1. Display an intro/welcome message to the player.
    print("""
    ._______________________.
    |_____Welcome to my_____|
    |_Number Guessing Game!_|
    |_______________________|""")

    # 2. Store a random number as the answer/solution.
    random_num = random.randint(1, 25)
    guesses = []

    player_guess = int(input("\nGuess a number between 1 and 25:  "))
    guesses.append(player_guess)
    # 3. Continuously prompt the player for a guess.
    while player_guess != random_num:
        #   a. If the guess greater than the solution, display to the player "It's lower".
        if player_guess < random_num:
            print("Too low!")
        #   b. If the guess is less than the solution, display to the player "It's higher".
        elif player_guess > random_num:
            print("Too high!")
        player_guess = int(input("Please try again:  "))
        guesses.append(player_guess)

    # 4. Once the guess is correct, stop looping, inform the user they "Got it"
    #    and show how many attempts it took them to get the correct number.
    print("\nCongratulations! You won in {} guesses.".format(len(guesses)))
    # 5. Let the player know the game is ending, or something that indicates the game is over.
    play_again = input("\nGame Over. Would you like to play again? (Y/N)  ").lower()
    if play_again == "y":
        start_game()


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
