def binary_search(list,target):
    left = 0
    right = len(list) - 1

    while left <= right :
        middle = (left + right)//2

        if list[middle] == target:
            return True

        elif list[middle] < target:
            left = middle + 1

        else:
            right =middle - 1

    return False

a = [2,5,7,9,12,15,16,18,19,34,58,87]
b = [1]
#Test Stage
print(binary_search(a,15))
print(binary_search(b,1))
