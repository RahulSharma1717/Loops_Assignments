# Create a simple calculator using loops (The program should be menu driven which runs till user exits itself.
# Means the program must ask the user every time to whether he want to continue or exit). Print Appropriate Message for this.(use while() loop)


def basic_calculator(number_1, number_2, operation):
    if operation == "ADD":
        print(f"Addition of the two input numbers is {number_1 + number_2}")
    elif operation == "SUB":
        print(f"Substraction of the two input numbers is {number_1 - number_2}")
    elif operation == "MUL":
        print(f"Multiplication of the two input numbers is {number_1 * number_2}")
    elif operation == "DIV":
        if number_2 != 0:
            print(f"Division of the two input numbers is {number_1 / number_2}")
        else:
            print("Zero Division Error, Enter a Non-Zero second number")
    else:
        print("Please enter a valid option from the menu")
    print()


while True:
    input_value = input("""Enter the operation to be performed (press 'Q' anytime to display the exit option))
    input "ADD" to perform addition
    input "SUB" to perform substraction
    input "MUL" to perform multiplication
    input "DIV" to perform division: """).upper()

    if input_value == "Q":
        quit_loop = input("Do you wish to continue; answer 'yes' or  'no': ")
        if quit_loop.lower() == "no":
            print()
            break
        else:
            print()
            continue

    valid_operations = ["ADD", "SUB", "MUL", "DIV", "Q"]
    if input_value not in valid_operations:
        print("Invalid option! Please enter a valid operation from the menu.")
        print()
        continue

    try:
        number_1 = float(input("Enter the First Number: "))
        number_2 = float(input("Enter the Second Number: "))
        basic_calculator(number_1, number_2, input_value)
    except ValueError:
        print("Invalid input! Please enter valid numeric values.")


"""Output:
Enter the operation to be performed (press 'Q' anytime to display the exit option))
    input "ADD" to perform addition
    input "SUB" to perform substraction
    input "MUL" to perform multiplication
    input "DIV" to perform division: ed
Invalid option! Please enter a valid operation from the menu.

Enter the operation to be performed (press 'Q' anytime to display the exit option))
    input "ADD" to perform addition
    input "SUB" to perform substraction
    input "MUL" to perform multiplication
    input "DIV" to perform division: qw
Invalid option! Please enter a valid operation from the menu.

Enter the operation to be performed (press 'Q' anytime to display the exit option))
    input "ADD" to perform addition
    input "SUB" to perform substraction
    input "MUL" to perform multiplication
    input "DIV" to perform division: div
Enter the First Number: 36
Enter the Second Number: 0
Zero Division Error, Enter a Non-Zero second number

Enter the operation to be performed (press 'Q' anytime to display the exit option))
    input "ADD" to perform addition
    input "SUB" to perform substraction
    input "MUL" to perform multiplication
    input "DIV" to perform division: add
Enter the First Number: 23
Enter the Second Number: 45
Addition of the two input numbers is 68.0

Enter the operation to be performed (press 'Q' anytime to display the exit option))
    input "ADD" to perform addition
    input "SUB" to perform substraction
    input "MUL" to perform multiplication
    input "DIV" to perform division: sub
Enter the First Number: -96
Enter the Second Number: -84
Substraction of the two input numbers is -12.0

Enter the operation to be performed (press 'Q' anytime to display the exit option))
    input "ADD" to perform addition
    input "SUB" to perform substraction
    input "MUL" to perform multiplication
    input "DIV" to perform division: -45
Invalid option! Please enter a valid operation from the menu.

Enter the operation to be performed (press 'Q' anytime to display the exit option))
    input "ADD" to perform addition
    input "SUB" to perform substraction
    input "MUL" to perform multiplication
    input "DIV" to perform division: div
Enter the First Number: -45
Enter the Second Number: 5
Division of the two input numbers is -9.0

Enter the operation to be performed (press 'Q' anytime to display the exit option))
    input "ADD" to perform addition
    input "SUB" to perform substraction
    input "MUL" to perform multiplication
    input "DIV" to perform division: q
Do you wish to continue; answer 'yes' or  'no': yes

Enter the operation to be performed (press 'Q' anytime to display the exit option))
    input "ADD" to perform addition
    input "SUB" to perform substraction
    input "MUL" to perform multiplication
    input "DIV" to perform division: mul
Enter the First Number: 45
Enter the Second Number: 89
Multiplication of the two input numbers is 4005.0

Enter the operation to be performed (press 'Q' anytime to display the exit option))
    input "ADD" to perform addition
    input "SUB" to perform substraction
    input "MUL" to perform multiplication
    input "DIV" to perform division: q
Do you wish to continue; answer 'yes' or  'no': no


Process finished with exit code 0
"""