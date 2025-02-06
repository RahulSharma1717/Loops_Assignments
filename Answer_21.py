# Create Rock, Paper, Scissor game using while loop
# (Hint- use random module and random.choice(['rock', 'paper', 'scissor']) function to get random value selected by computer)
# Your Program will contain one you and second the computer who will be generating the values from its side using random module.
# User will provide the choice of Rock, paper or scissor.
# Print Appropriate Messages and final score of both the computer and user.

import random

def rock_paper_scissor():
    choices = ["rock", "paper", "scissor"]
    user_score = 0
    computer_score = 0
    print("\nRock, Paper, Scissors Game!")

    while True:
        print()
        user_choice = input("Enter your choice (rock, paper, scissor) or 'q' to quit: ").lower()

        if user_choice == "q":
            print("\nGame Over!")
            print(f"Final Score -> You: {user_score}, Computer: {computer_score}")
            break

        if user_choice not in choices:
            print("Invalid choice! Please choose rock, paper, or scissor.")
            continue

        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissor") or \
                (user_choice == "paper" and computer_choice == "rock") or \
                (user_choice == "scissor" and computer_choice == "paper"):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Current Score -> You: {user_score}, Computer: {computer_score}")

rock_paper_scissor()



"""Output:
Rock, Paper, Scissors Game!
Enter your choice (rock, paper, scissor) or 'q' to quit: paper
Computer chose: scissor
Computer wins this round!
Current Score -> You: 0, Computer: 1

Rock, Paper, Scissors Game!
Enter your choice (rock, paper, scissor) or 'q' to quit: rock
Computer chose: scissor
You win this round!
Current Score -> You: 1, Computer: 1

Rock, Paper, Scissors Game!
Enter your choice (rock, paper, scissor) or 'q' to quit: paper
Computer chose: rock
You win this round!
Current Score -> You: 2, Computer: 1

Rock, Paper, Scissors Game!
Enter your choice (rock, paper, scissor) or 'q' to quit: q

Game Over!
Final Score -> You: 2, Computer: 1
"""