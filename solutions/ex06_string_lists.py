"""
Ask the user for a string and print out whether this string is a palindrome or not. 
(A palindrome is a string that reads the same forwards and backwards.)
"""


def is_palindrome(word):
    for i in range(len(word)//2):
        if word[i] != word[-(i+1)]:
            return f"{word} is not palindrome"
    return f"{word} is palindrome"


#Test Stage
print(is_palindrome("code"))
print(is_palindrome("sos"))