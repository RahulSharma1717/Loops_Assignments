# Write a program to count the number of alphabets and no of digits in a string using loops.

def count_characters(str):
    count_alphabet = 0
    count_digit = 0
    invalid_characters = ""
    for char in str:
        if char.isalpha():
            count_alphabet += 1
        elif char.isnumeric():
            count_digit += 1
        elif char != " ":
            invalid_characters += char

    print(f"The invalid characters entered are '{' '.join(invalid_characters)}'")
    return f"Number of alphabets and numerals are {count_alphabet} and {count_digit} respectively"

input_string = input("Enter alphanemeric characters of your choice: ")
counts = count_characters(input_string)
print(counts)


"""Output:
Enter alphanemeric characters of your choice: sw 52 de 78s45 67 + ? < fg
The invalid characters entered are '+ ? <'
Number of alphabets and numerals are 7 and 8 respectively
"""