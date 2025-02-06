# Write a program to reverse the String using while loop.

input_string = input("\nEnter a string of your choice: ")
string_length = len(input_string)
reversed_string = ""
i = 0

while i < string_length:
    reversed_string += input_string[string_length - i - 1]
    i += 1

print(f"\nThe reversed string is: {reversed_string}")


"""Output:
Enter a string of your choice: Write a program to reverse the String using while loop.

The reversed string is: .pool elihw gnisu gnirtS eht esrever ot margorp a etirW
"""