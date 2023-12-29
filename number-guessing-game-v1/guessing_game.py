"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""

import random

def start_game():
    print("Welcome to the Number Guessing Game!")
    print("Try to guess the number between 1 and 100.")

    # Initialize game variables
    high_score = float('inf')  # Initialize high score to positive infinity

    while True:
        print(f"\nCurrent High Score: {high_score}")
        print("1. Play Game")
        print("2. Quit")

        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            play_game(high_score)
        elif choice == "2":
            print("Thanks for playing! Goodbye.")
            break
        else:
            print("Invalid choice. Please enter 1 or 2.")

def play_game(high_score):
    solution = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("\nEnter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Invalid option. Please enter a number between 1 and 100.")
            elif guess < solution:
                print("It's higher.")
            elif guess > solution:
                print("It's lower.")
            else:
                print("Congratulations! You guessed the correct number in {} attempts.".format(attempts))
                if attempts < high_score:
                    print("New High Score!")
                play_again = input("Do you want to play again? (yes/no): ").lower()
                if play_again == "yes":
                    return
                else:
                    print("Thanks for playing! Goodbye.")
                    exit()

        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    start_game()


# Write your code inside this function.

#   When the program starts, we want to:
#   ------------------------------------
#   1. Display an intro/welcome message to the player.
#   2. Store a random number as the answer/solution.
#   3. Continuously prompt the player for a guess.
#     a. If the guess is greater than the solution, display to the player "It's lower".
#     b. If the guess is less than the solution, display to the player "It's higher".

#   4. Once the guess is correct, stop looping, inform the user they "Got it"
#      and show how many attempts it took them to get the correct number.
#   5. Let the player know the game is ending, or something that indicates the game is over.

# ( You can add more features/enhancements if you'd like to. )


# Kick off the program by calling the start_game function.
