"""
Write a password generator in Python. Be creative with how you 
generate passwords - strong passwords have a mix of lowercase letters, 
uppercase letters, numbers, and symbols. The passwords should be random, 
generating a new password every time the user asks for a new password. Include your run-time code in a main method.

Extra:

Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.

"""
import random
import string
def password_generator(strong):
    words = ['green','red','orange','purple','blue']

    if strong == "weak":
        word1 = random.choice(words)
        word2 = random.choice(words)
        number = random.randint(10,99)
        return word1 + word2 + str(number)

    else:
        letters = "abcdefghijklmnopqrstuvwxyz"
        big_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "0123456789"
        special_characters = "!@#$%&"
        all_characters = letters + big_letters + numbers + special_characters

        password = []
        for i in range(16):
            password.append(random.choice(all_characters))

        return "".join(password)

#Test Stage
print(password_generator("strong"))