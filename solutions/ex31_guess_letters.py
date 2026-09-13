word = "EVAPORATE"

def display(word, guessed_letters):
    return ' '.join(
        letter if letter in guessed_letters else '_' for letter in word
    )

def guess_letter():
    guessed_letters = set()

    print("Welcome to Hangman! ")

    while True:
        print(display(word, guessed_letters))

        guess = input("Guess your letter: ").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter")
            continue

        if guess in guessed_letters:
            print("Please enter not guessed letter")
            continue

        guessed_letters.add(guess)

        if guess not in word:
            print("Incorrect!")

print(guess_letter())