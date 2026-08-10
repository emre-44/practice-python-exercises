import random
"""
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, 
then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use 
the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""


def guess_number():
    number = random.randint(1, 9)
    step = 0
    while (True):
        guess = int(input("Guess the number:  "))
        step += 1
        if guess != number:
            if guess > number:
                print("You guessed to high!")

            else:
                print("You guessed to low!")

        else:
            print(f"Congrulations!!! You found the number on {step} steps")
            quit = input("Do you want quit game? (Y) yes, (N) no : ")
            if quit == "Y":
                break

# Test Stage
guess_number()
