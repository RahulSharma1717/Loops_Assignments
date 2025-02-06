# Write a program to check whether the given number is palindrome or not.
# Example : 343, 121, 111, etc.


def palindrome_number(num):
    try:
        reversed_num = 0
        temp = int(num)
        while temp > 0:
            digit = temp % 10
            reversed_num = (reversed_num * 10) + digit
            temp = temp // 10

        if reversed_num == int(num):
            return f"Input number '{num}' is a Palindrome"
        else:
            return f"Input number '{num}' is not a Palindrome"

    except ValueError:
        return "Invalid Input!, Enter a numeric value"


input_value = input("Enter the number to be checked: ")
check_palindrome = palindrome_number(input_value)
print(check_palindrome)


"""Output:
Enter the number to be checked: 1234321
Input number '1234321' is a Palindrome
"""

"""Output:
Enter the number to be checked: abc
Invalid Input!, Enter a numeric value
"""