"""
Create a program that will play the “cows and bulls” game with the user. The game works like this:

Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout the game and tell the user at the end.
"""

import random

def cows_and_bulls():
    number = random.randint(1000, 9999)
    number_str = str(number)
    
    print("Welcome to Cows and Bulls Game!")
    print()
    
    guess_count = 0
    
    while True:
        guess = input("Enter your 4-digit guess (or 'quit' to exit): ")
        
        if guess.lower() == 'quit':
            print(f"\nGame ended. The number was: {number_str}")
            print("Thanks for playing!")
            return
        
        if len(guess) != 4 or not guess.isdigit():
            print("Invalid input! Please enter exactly 4 digits (0-9).")
            continue
        
        guess_str = str(guess)
        guess_count += 1
        
        cows = 0
        for i in range(4):
            if number_str[i] == guess_str[i]:
                cows += 1
        
        num_list = list(number_str)
        guess_list = list(guess_str)
        
        for i in range(4):
            if num_list[i] == guess_list[i]:
                num_list[i] = None
                guess_list[i] = None
        
        bulls = 0
        for i in range(4):
            if guess_list[i] is not None and guess_list[i] in num_list:
                bulls += 1
                index = num_list.index(guess_list[i])
                num_list[index] = None
        
        print(f"Guess #{guess_count}: {guess_str}")
        print(f"Cows: {cows}, Bulls: {bulls}")
        print()
        
        if cows == 4:
            print(f"Congratulations! You guessed it!")
            print(f"The number was: {number_str}")
            print(f"You found it in {guess_count} guesses!")
            break

if __name__ == "__main__":
    cows_and_bulls()

    
