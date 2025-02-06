# Print a simple multiplication table of number given by user input.

number = int(input("Enter the number whose multiplication table you want: "))
i = 1

while i <= 10:
    print(number * i, end=' ')
    i += 1


"""Output:
Enter the number whose multiplication table you want: 2
2 4 6 8 10 12 14 16 18 20 
"""

"""Output:
Enter the number whose multiplication table you want: 139
139 278 417 556 695 834 973 1112 1251 1390 
"""