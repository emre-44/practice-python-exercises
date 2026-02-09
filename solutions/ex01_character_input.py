"""
Exercise 1: Character Input

Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that 
they will turn 100 years old.

Extras:

Add on to the previous program by asking the user for another number 
and printing out that many copies of the previous message. 
Print out that many copies of the previous message on separate lines. 
"""
from datetime import datetime


def calculate_100_year():
    """
    Calculate the year when someone turns 100 years old.

    Args:

    Returns:
        int: The year when the person will be 100 years old    

    """
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    count = int(input("Enter message count: "))

    current_year = datetime.now().year
    when_100_year = current_year + (100 - age)
    for _ in range(count):
        print(f"{name} will be 100 years old in {when_100_year}")

    print(f"Message printed {count} times.")
    return when_100_year

#Test Stage
print(calculate_100_year())
