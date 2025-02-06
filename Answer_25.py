# Write a Python program to check the validity of passwords input by users.
#     Validation :
#     At least 1 letter between [a-z] and 1 letter between [A-Z].
#     At least 1 number between [0-9].
#     At least 1 character from [$#@].
#     Minimum length 6 characters.
#     Maximum length 16 characters.

def is_valid_password(password):
    has_lower = has_upper = has_digit = has_special = False
    special_chars = "$#@"
    is_valid = True

    if not (6 <= len(password) <= 16):
        print("Password must be between 6 and 16 characters long")
        is_valid = False

    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True

    if not has_lower:
        print("Password must contain at least one lowercase letter (a-z)")
        is_valid = False
    if not has_upper:
        print("Password must contain at least one uppercase letter (A-Z)")
        is_valid = False
    if not has_digit:
        print("Password must contain at least one digit (0-9)")
        is_valid = False
    if not has_special:
        print("Password must contain at least one special character ($, #, or @)")
        is_valid = False

    return is_valid


while True:
    password = input("\nEnter a password: ")

    if is_valid_password(password):
        print("Your password is valid!")
        break
    else:
        print("Please try again with a valid password.")


"""Output:
Enter a password: rfdt
Password must be between 6 and 16 characters long
Password must contain at least one uppercase letter (A-Z)
Password must contain at least one digit (0-9)
Password must contain at least one special character ($, #, or @)
Please try again with a valid password.

Enter a password: weasq1247@
Password must contain at least one uppercase letter (A-Z)
Please try again with a valid password.

Enter a password: AQc3414$
Your password is valid!
"""




