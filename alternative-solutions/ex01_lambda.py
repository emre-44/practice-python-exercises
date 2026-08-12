from datetime import datetime

calculate_year = lambda age : datetime.now().year + (100 - age)
print_messsage = lambda name, year, count : [print(f"{name} will be 100 years old in {year}") for _ in range(count)]

def calculate_100_year():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    count = int(input("Enter message count: "))

    year = calculate_year(age)
    print_messsage(name, year, count)

    print(f"Message printed {count} times.")
    return year

#Test Stage
calculate_100_year()