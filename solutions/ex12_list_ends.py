"""
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.
"""
import random

def list_ends(list_input):
    new_list = [list_input[0],list_input[-1]]
    random.shuffle(new_list)
    return new_list

list_input = [5, 10, 15, 20, 25]

#Test stage
print(list_ends(list_input))
