# This is my Rock-Paper-Scissors game implementation

print("Welcome to Rock-Paper-Scissors!")

import random

player_choice = input("Enter your choice (rock, paper, scissors): ").lower()
computer_choice = random.choice(["rock", "paper", "scissors"])

print(f"Computer chose: {computer_choice}")
print(f"You chose: {player_choice}")

#todo: Implement game logic to determine the winnner
