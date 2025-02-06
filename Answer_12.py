# Write a python program to check whether a number given by user is a special number or not.
# A special number is the number if the sum of the factorial of its digit is same as the original number. Example : 145

def factorial_of_number(n):
    number = n
    i = 1
    factorial = 1

    while i <= number:
        factorial = factorial * i
        i = i + 1

    return factorial

special_number = input("Enter a number: ")

if not special_number.isdigit():
    print("Invalid input! Please enter a valid positive integer.")
else:
    sum_of_factorials = 0
    for char in special_number:
        print(char, end=" ")
        int_char = int(char)
        sum_of_factorials = sum_of_factorials + factorial_of_number(int_char)

    print()

    if sum_of_factorials == int(special_number):
        print(f"The entered number '{special_number}' is a special number. The sum of the factorial of its digit is also '{sum_of_factorials}'")
    else:
        print(f"The entered number '{special_number}' is not a special number")
