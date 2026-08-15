"""
Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order
"""

def reverse_words(text):
    words = text.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

#Test Stage
print(reverse_words("world! Hello"))
