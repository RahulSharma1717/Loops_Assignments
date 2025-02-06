# Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input ). Print average and product of all numbers.

sum = 0
product = 1

while True:
    input_value = input("Enter the number (press 'q' anytime to go to the quit options menu) : ")
    print()
    if input_value.lower() == "q":
        quit_loop = input("Do you want to quit; answer 'yes' or  'no': ")
        if quit_loop.lower() == "yes":
            print()
            break
        else:
            print()
            continue

    try:
        sum = sum + int(input_value)
        product = product * int(input_value)
    except ValueError:
        print("Invalid input! Please enter an integer or 'q'")
        print()

if sum == 0 and product == 1:
    print("No valid numbers were entered.")
else:
    print(f"Sum is {sum}")
    print(f"Product is {product}")


"""Output:
Enter the number (press 'q' anytime to go to the quit options menu) : q

Do you want to quit; answer 'yes' or  'no': se

Enter the number (press 'q' anytime to go to the quit options menu) : 89

Enter the number (press 'q' anytime to go to the quit options menu) : 25

Enter the number (press 'q' anytime to go to the quit options menu) : 63

Enter the number (press 'q' anytime to go to the quit options menu) : q

Do you want to quit; answer 'yes' or  'no': no

Enter the number (press 'q' anytime to go to the quit options menu) : 78

Enter the number (press 'q' anytime to go to the quit options menu) : 12

Enter the number (press 'q' anytime to go to the quit options menu) : q

Do you want to quit; answer 'yes' or  'no': yes

Sum is 267
Product is 131203800"""




