# Write a program to check whether the given string is palindrome or not.
# Example : MADAM, MOM

def palindrome_string(str):
    if str == str[::-1]:
        print(f"Indexing: The input string '{str}' is a palindrome")
    else:
        print(f"Indexing: The input string '{str}' is not a palindrome")


def palindrome_using_loop(str):
    string_length = len(str)
    reversed_string = ""
    i = 0

    while i < string_length:
        reversed_string += str[string_length - i - 1]
        i += 1

    if reversed_string == str:
        return f"Looping: String '{str}' is a Palindrome"
    else:
        return f"Looping: String '{str}' is not a Palindrome"


input_string = input("Enter a string of your choice: ").upper()
print()
palindrome_string(input_string)
using_loop = palindrome_using_loop(input_string)
print(using_loop)


"""Output:
Enter a string of your choice: racecar

Indexing: The input string 'RACECAR' is a palindrome
Looping: String 'RACECAR' is a Palindrome
"""

"""Output:
Enter a string of your choice: 1234321

Indexing: The input string '1234321' is a palindrome
Looping: String '1234321' is a Palindrome
"""