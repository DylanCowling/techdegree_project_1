import random


def start_game():
    # Display an intro/welcome message to the player.
    print("""
    ._______________________.
    |_____Welcome to my_____|
    |_Number Guessing Game!_|
    |_______________________|""")

    # Store a random number as the answer/solution.
    random_num = random.randint(1, 25)
    guesses = []
    try:
        player_guess = int(input("\nGuess a number between 1 and 25:  "))
        guesses.append(player_guess)
        # Continuously prompt the player for a guess.
        while player_guess != random_num:
            # Make sure the player can try again if they guess outside of the number range.
            if player_guess > 25 or player_guess < 1:
                guesses.append(player_guess)
                player_guess = int(input("The number you guessed is not within 1 and 25, give it another shot:  "))
            #   If the guess greater than the solution, display to the player "It's lower".
            else:
                if player_guess < random_num:
                    print("Too low!")
                #   If the guess is less than the solution, display to the player "It's higher".
                elif player_guess > random_num:
                    print("Too high!")
                player_guess = int(input("Please try again:  "))
                guesses.append(player_guess)
    except ValueError as err:
        print("Oh no! It looks like something went wrong...")
        print("({})".format(err))
    else:
        # Once the guess is correct, stop looping, inform the user they "Got it"
        # and show how many attempts it took them to get the correct number.
        print("\nCongratulations! You got it in {} guesses.".format(len(guesses)))
        # Let the player know the game is ending, or something that indicates the game is over.
    play_again = input("\nWould you like to play again? (Y/N)  ").lower()
    if play_again == "y":
        start_game()


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()

