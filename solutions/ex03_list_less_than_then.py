"""
Take a list, say for example this one:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

and write a program that prints out all the elements of the list that are less than 5.

Extras:

    Instead of printing the elements one by one, make a new list 
    that has all the elements less than 5 from this list in it and print out this new list.
    Write this in one line of Python.
    Ask the user for a number and return a list that contains only elements 
    from the original list a that are smaller than that number given by the user.

"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


def list_elements_less_than_5(user_list):
    """
    Find less than 5 elements in input list

    Args:
        a: Users list
    
    Returns
        list: List of elements less than 5

    """
    less_than_5_list = []

    for element in user_list:
        if element < 5:
            less_than_5_list.append(element)

    return less_than_5_list

# Test stage
print(list_elements_less_than_5(a))
