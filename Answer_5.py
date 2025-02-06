# Create a game 'Guess the number' Game. Let us go through Rules one by one.
#
# 1.Computer will generate a Random Number.
# 2.Ask user to guess the number in 10 chances.
# 3.If user guesses it right , Score him accordingly like if user guesses in first chance score is 100 , in second chance score should be 90 and so on.
# 4.If guess number is greater than random number give him 'Hint : Choose a Lower Number' or less than random number give him
# 'hint : Choose a Higher Number' or if guess number is equal to random , No need to hint , just display score and end the game.
# 5.Also show how many chances are left.
# 6.if user could not guess the number, disclose the random number and end the game.

import random

def guess_the_number():
    random_number = random.randint(1, 100)
    i = 0
    while i < 10:
        print(f"Number of chances left --- {(10 - i)}")
        guess = int(input("Guess the number in between 1 to 100: "))
        i += 1
        if i == 10:
            print(f"Sorry! You have ran out of chances, the Random Number is {random_number}")
        elif guess == random_number:
            print(f"You have guessed the random number '{random_number}' right")
            print(f"Your score is {110 - (10 * i)}")
            return
        elif guess > random_number:
            print('Hint : Choose a Lower Number\n')
        else:
            print('Hint : Choose a Greater Number\n')

guess_the_number()


"""Output:
Number of chances left --- 10
Guess the number in between 1 to 100: 50
Hint : Choose a Greater Number
Number of chances left --- 9
Guess the number in between 1 to 100: 65
Hint : Choose a Lower Number
Number of chances left --- 8
Guess the number in between 1 to 100: 55
Hint : Choose a Lower Number
Number of chances left --- 7
Guess the number in between 1 to 100: 52
Hint : Choose a Lower Number
Number of chances left --- 6
Guess the number in between 1 to 100: 51
You have guessed the random number '51' right
Your score is 60
"""

