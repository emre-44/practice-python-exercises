"""
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that 
are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:

Randomly generate two lists to test this
Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

"""

def generate_lists(a,b):

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
    return both_list

#Test Stage
print(generate_lists(5,3))
