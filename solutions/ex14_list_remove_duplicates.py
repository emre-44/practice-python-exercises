"""
Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different function.

"""

def remove_duplicates(a,b):

    list1 = []
    list2 = []
    both_list = []
    for i in range(a):
        if len(list1) < a:
            element1 = input(f"Write {i+1}. element for first list: ")
            list1.append(element1)

    for i in range(b):
        if len(list2) < b:
            element2 = input(f"Write {i+1}. element for second list: ")
            list2.append(element2)

    for element in list1:
        if element in list2 and element not in both_list:
            both_list.append(element)
    return set(both_list)

#Test Stage
print(remove_duplicates(5,3))
