is_even = lambda x : x % 2 == 0
is_multiple_of_4 = lambda x : x % 4 == 0
divides_evenly = lambda x,y : x % y == 0

def odd_or_even(number):
    if is_multiple_of_4(number):
        print(f"{number} is multiple of 4")
    elif is_even(number):
        print(f"{number} is even")
    else:
        print(f"{number} is odd")

def check_divisibility(number, check):
    if divides_evenly(number,check):
        print(f"{number} divides evenly into {check}!")
    else:
        print(f"{number} does not divide evenly into {check}!")

#Test Stage
print(odd_or_even(19))
print(check_divisibility(20,8))
