"""
Create a program that asks the user for a number and 
then prints out a list of all the divisors of that number. 
(If you don’t know what a divisor is, it is a number that divides evenly 
into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
"""

def divisors():
    """
    Find divisors from user input

    Returns:
        list: List of divisors

    """
    divisors_list = []
    try:
        number = int(input("Enter the number: "))
        for x in range(1,(number//2)+1):
            if number % x == 0:
                divisors_list.append(x)

        divisors_list.append(number)

    except ValueError:
        print("Please enter a valid integer")
        return []

    except ZeroDivisionError:
        print("Zero has infinite divisors. Enter a non-zero number")
        return []

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

    return divisors_list

# Test stage
print(divisors())
