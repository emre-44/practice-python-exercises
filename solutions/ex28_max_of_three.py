def find_max():
    numbers_str = (input("Input three number: ").split())
    numbers = list(map(int, numbers_str))

    print(f"{max(numbers)} is biggest number")


print(find_max())