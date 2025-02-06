# Write a program that prints the Fibonacci sequence up to a given number using a while loop.

max_value = int(input("Enter the maximum number for the Fibonacci sequence: "))

a, b = 0, 1

print("Fibonacci Sequence:")
while a <= max_value:
    print(a, end=" ")
    a, b = b, a + b


"""Output:
Enter the maximum number for the Fibonacci sequence: 100
Fibonacci Sequence:
0 1 1 2 3 5 8 13 21 34 55 89 
"""