import random

def load_words():
    with open('ex30_SOWPODS.txt','r') as open_file:
        return open_file.read().splitlines()
    
all_words = load_words()

def random_word():
    word = random.choice(all_words)
    return word

def display(word, guessed_letters):
    return ' '.join(
        letter if letter in guessed_letters else '_' for letter in word
    )

def guess_letter():
    guessed_letters = set()
    word = random_word()
    wrong_count = 0
    max_wrong_count = 6
    print("Welcome to Hangman! ")

    while wrong_count < max_wrong_count:
        print(display(word, guessed_letters))

        guess = input("Guess your letter: ").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter")
            continue

        if guess in guessed_letters:
            print("Please enter not guessed letter")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("Corrcet!")
            if all(l in guessed_letters for l in word):
                print(display(word, guessed_letters))
                print("You won!")
                return
        else:
            wrong_count += 1
            print("Incorrect")
            wrong_guess(wrong_count)
    print(f"Game over! The word was: {word}")
           
def wrong_guess(attempts):
    stages = [
        "",
        " O ",
        " O \n | ",
        " O \n/| ",
        " O \n/|\\ ",
        " O \n/|\\ \n/  ",
        " O \n/|\\ \n/ \\ ",
    ]
    print(stages[attempts])
        
print(guess_letter())