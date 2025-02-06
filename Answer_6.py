# Find all prime numbers between 1 to 2000

def prime_numbers(a, b):
    for num in range(a, b+1):
        count = 0
        for i in range(2, num):
            if num % i == 0:
                count += 1
        if count == 0 and num > 1:
            print(num, end=" ")

print(prime_numbers(1, 2000))
