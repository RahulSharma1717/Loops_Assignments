# Write a program to print the even and odd numbers in the range from 1 to n where n is given by the user
# and also print the sum of all even numbers and odd numbers separately.(use while loop)

try:
    n = int(input("Enter the number till where you want the find the even and odd numbers: "))
    odd_numbers = []
    even_numbers = []
    odd_numbers_sum = 0
    even_numbers_sum = 0
    i = 1

    while i < n:
        if i % 2 == 0:
            even_numbers.append(i)
            even_numbers_sum += i
        else:
            odd_numbers.append(i)
            odd_numbers_sum += i
        i += 1

    print(f"Even numbers uptill '{n}' are {even_numbers}")
    print(f"Odd numbers uptill '{n}' are {odd_numbers}")
    print(f"Sum of even numbers: {even_numbers_sum}")
    print(f"Sum of odd numbers: {odd_numbers_sum}")

except ValueError:
    print("Please enter a numeric input")


"""Output:
Enter the number till where you want the find the even and odd numbers: 99
Even numbers uptill '99' are [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98]
Odd numbers uptill '99' are [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97]
Sum of even numbers: 2450
Sum of odd numbers: 2401
"""
