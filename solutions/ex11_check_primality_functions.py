"""
Ask the user for a number and determine whether the number is prime or not. 
(For those who have forgotten, a prime number is a number that has no divisors.). 
You can (and should!) use your answer to Exercise 4 to help you. Take this opportunity 
to practice using functions, described below.
"""


def check_primality(num):
    if num < 2:
        return f"{num} is not prime"
    
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            return f"{num} is not prime"
    
    return f"{num} is prime"

#Test Stage
print(check_primality(15))