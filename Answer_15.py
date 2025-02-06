# Write a program to check whether the number is automorphic number or not.
# (A number is said to be automorphic number if the original number is present on the right of the square of that number)

def is_automorphic(input_number):
    square = input_number ** 2
    temp_num = input_number
    temp_square = square

    while temp_num > 0:
        if temp_num % 10 != temp_square % 10:
            print(f"The number '{input_number}' is not automorphic with its square '{square}'")
            return
        temp_num = temp_num // 10
        temp_square = temp_square // 10

    print(f"The number '{input_number}' is automorphic with its square '{square}'")

try:
    number = int(input("Enter a number: "))
    is_automorphic(number)
except ValueError:
    print("Invalid Input! Enter a valid numeric value.")


"""Output:
Enter a number: 625
The number '625' is automorphic with its square '390625'
"""

