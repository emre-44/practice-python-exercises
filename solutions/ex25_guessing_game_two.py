"""
As the writer of this program, you will have to choose how your program will strategically guess. A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) until you hit the number. But that’s not an optimal guessing strategy. An alternate strategy might be to guess 50 (right in the middle of the range), and then increase / decrease by 1 as needed. After you’ve written the program, try to find the optimal strategy! 
"""

def guess_number():
    print("Choose number between 0 and 100!")
    min = 0
    mid = 50
    max = 100
    answer = ""
    while True:
        answer = input(f"Is your number {mid}? Y/N: ")
        if answer == "Y":
            return True
        else:
            answer = input(f"Is your number bigger than {mid}? Y/N: ")
            if answer == "Y":
                min = mid
                mid = (mid + max) // 2
            else:
                max = mid
                mid = (mid + min) // 2
        
print(guess_number())