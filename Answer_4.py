# Take 10 values from user and find out the sum and multiplication and average of the numbers.

try:
    i = 1
    numbers = []
    product = 1
    while i <= 10:
        values = float(input(f"Enter numeric value No. {i}: "))
        numbers.append(values)
        product = product * values
        i += 1
except ValueError:
    print("Invalid Input!, Enter only Numeric Values")

sum_of_numbers = sum(numbers)
print(f"The Sum of numbers is {sum_of_numbers}")
multiplication_of_numbers = product
print(f"The Product of numbers is {multiplication_of_numbers}")
average_of_numbers = sum_of_numbers / i - 1
print(f"The Average of numbers is {average_of_numbers}")


"""Output:
Enter numeric value No. 1: 52
Enter numeric value No. 2: 21
Enter numeric value No. 3: 14
Enter numeric value No. 4: b
Invalid Input!, Enter only Numeric Values
The Sum of numbers is 87.0
The Product of numbers is 15288.0
The Average of numbers is 20.75
"""

"""Here the program concludes when a wrong input is fed. In file Answer_4a trying to write a code that continues execution even after wrong input"""