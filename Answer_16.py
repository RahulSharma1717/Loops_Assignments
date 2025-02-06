# Write a program to reverse a number taken by the user without using strings.

def reverse_number(n):
    reversed_num = 0
    while n > 0:
        last_digit = n % 10
        reversed_num = (reversed_num * 10) + last_digit
        n //= 10
    return reversed_num

num = int(input("Enter a number: "))

reversed_num = reverse_number(num)
print(f"Reversed number: {reversed_num}")


"""Output:
Enter a number: 89657124
Reversed number: 42175698
"""
