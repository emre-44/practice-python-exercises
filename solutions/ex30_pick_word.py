import random

def load_words():
    with open('ex30_SOWPODS.txt','r') as open_file:
        return open_file.read().splitlines()
    
all_words = load_words()

def random_word():
    return random.choice(all_words)

#Test Stage
print(random_word())