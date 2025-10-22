"""
WORKFLOW OF PROJECT:
1 - Input from user(Rock, Paper, Scissors)
2- computer choice (computer will choose randomly not conditionally)
3 - Result Print

Cases:
A- rock
rock - rock = draw
rock - paper = lose
rock - scissors = win

B - paper
paper - rock = win
paper - paper = draw
paper - scissors = lose

C- scissors
scissors - rock = lose
scissors - paper = win
scissors - scissors = draw

"""

import random

item_list = ["rock", "paper", "scissors"]
user_choice = input("Enter your move (rock, paper, scissors): ").lower()
computer_choice = random.choice(item_list)

print(f"user choice: {user_choice}, computer choice: {computer_choice}")
if user_choice == computer_choice:
    print("It's a draw!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
     (user_choice == "paper" and computer_choice == "rock") or \
     (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
    
else:
    print("You lose!")

