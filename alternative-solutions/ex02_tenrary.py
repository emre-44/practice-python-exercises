def check_odd_or_even(number):
    message = f"{number} is even and a multiple of 4" if number % 4 == 0 else f"{number} is even" if number % 2 == 0 else f"{number} is odd!"
    print(message)
def check_divisibility(num, check):
    print(f"{num} {'divides'if num % check == 0 else 'does not divide'} evenly into {check}")

#Test Stage
print(check_odd_or_even(23))
print(check_divisibility(28,4))
