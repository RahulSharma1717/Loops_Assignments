# Take 10 values from user and find out the sum and multiplication and average of the numbers.

def get_valid_number(i):
    """Function to take valid numeric input"""
    while True:
        try:
            value = float(input(f"Enter numeric value No. {i}: "))
            return value  # Return the valid number
        except ValueError:
            print("Invalid Input! Please enter only numeric values.")

numbers = []
product = 1

for i in range(1, 11):  # Loop to take 10 values
    value = get_valid_number(i)  # Get valid number
    numbers.append(value)
    product *= value  # Multiply the values

sum_of_numbers = sum(numbers)
average_of_numbers = sum_of_numbers / 10

print(f"\nThe Sum of 10 numbers is {sum_of_numbers}")
print(f"The Product of 10 numbers is {product}")
print(f"The Average of 10 numbers is {average_of_numbers}")


"""Output:
Enter numeric value No. 1: 25
Enter numeric value No. 2: 64
Enter numeric value No. 3: c
Invalid Input! Please enter only numeric values.
Enter numeric value No. 3: 14
Enter numeric value No. 4: 23
Enter numeric value No. 5: 85
Enter numeric value No. 6: 20
Enter numeric value No. 7: 32
Enter numeric value No. 8: 41
Enter numeric value No. 9: 3
Enter numeric value No. 10: 5

The Sum of 10 numbers is 312.0
The Product of 10 numbers is 17236531200000.0
The Average of 10 numbers is 31.2
"""