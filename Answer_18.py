# Write a program to check whether the number given by the user is an Armstrong number or not.
# (An Armstrong number is the number whose digits cubes sum is equal to the original number. Such as 153 as 1^3 + 5^3+3^3 = 1 + 125 + 27 = 153)

import sys

def Armstrong_Number(user_input):
    try:
        number = int(user_input)
        no_of_digits = len(user_input)
        last_digit = 0
        digits_sum = 0
        i = 0

        while number > 0:
            last_digit = number % 10
            digits_sum = digits_sum + last_digit ** no_of_digits
            remaining_number = number // 10
            number = remaining_number
            i = i + 1
        return digits_sum

    except ValueError:
        print("Invalid Input!, Enter numeric values")
        sys.exit()

user_input = input("Enter a number: ")
armstrong_sum = Armstrong_Number(user_input)

if int(user_input) == armstrong_sum:
    print(f"Entered number '{user_input}' is an Armstrong number with sum  of digits equalling '{armstrong_sum}'")
else:
    print(f"Entered number '{user_input}' is not an Armstrong number with sum of digits equalling '{armstrong_sum}'")


"""Output:
Enter a number: 9474
Entered number '9474' is an Armstrong number with sum  of digits equalling '9474'
"""

"""Output:
Enter a number: 1000
Entered number '1000' is not an Armstrong number with sum of digits equalling '1'
"""

"""Output:
Enter a number: a
Invalid Input!, Enter numeric values
"""

