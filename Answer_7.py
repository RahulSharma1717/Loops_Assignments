# Take a number from user and return sum of all digits of the number.

number = input("Enter a number: ")
sum = 0

try:
    for num in number:
        last_digit = int(num) % 10
        remaining_number = int(num) // 10
        number = remaining_number
        sum += last_digit
        print(f"The sum of the digits of number is {sum}")
except ValueError:
    print("Invalid Input!, Enter a positive numeral")



