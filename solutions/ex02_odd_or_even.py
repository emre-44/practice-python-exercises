"""
Exercise 2: Odd Or Even
Ask the user for a number. Depending on whether the number is even or odd, 
print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""


def check_odd_even(number):
    if number % 2 == 0:
        if number % 4 == 0:
            print(f"{number} is even and a multiple of 4")
        else:
            print(f"{number} is even")
    else:
        print(f"{number} is odd!")


def check_divisibility(num, check):
    if (num % check == 0):
        print(f"{check} divides evenly into {num}!")
    else:
        print(f"{check} does not divide evenly into {num}!")


check_odd_even(15)
check_odd_even(2)
check_divisibility(1984, 4)
