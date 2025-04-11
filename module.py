import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors", "lizard", "spock"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"

    winning_combos = {
        "rock": ["scissors", "lizard"],
        "paper": ["rock", "spock"],
        "scissors": ["paper", "lizard"],
        "lizard": ["spock", "paper"],
        "spock": ["scissors", "rock"]
    }

    if computer_choice in winning_combos[user_choice]:
        return "You win!"
    else:
        return "Computer wins!"
