# Do you know Factorial ? It is the product of an integer and all the integers below it;
# e.g. factorial four ( 4! ) is equal to 24. Take a number from user and calculate factorial of a number.

try:
    number = int(input("Enter a number you wish to calculate factorial for: "))
    i = 1
    factorial = 1

    while i <= number:
        factorial = factorial * i
        i = i + 1

    print(factorial)

except ValueError:
    print("Invalid Input! Enter a Valid Input")