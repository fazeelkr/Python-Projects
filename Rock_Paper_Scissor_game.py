import random

take_input = input("Enter Rock, Paper, or Scissors: ").capitalize()

rock = '''    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper = '''    _______
---'   ____)____
           ______)
          _______)
         _______)
---.__________)'''

scissors = '''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

game = ["Rock", "Paper", "Scissors"]

if take_input not in game:
    print("Invalid input")
    exit()

computer_choice = random.choice(game)

# Print user's choice
if take_input == "Rock":
    print(rock)
elif take_input == "Paper":
    print(paper)
elif take_input == "Scissors":
    print(scissors)

# Print computer's choice
if computer_choice == "Rock":
    print("Computer chose Rock")
    print(rock)
elif computer_choice == "Paper":
    print("Computer chose Paper")
    print(paper)
else:
    print("Computer chose Scissors")
    print(scissors)

# Decide the winner
if take_input == computer_choice:
    print("It's a draw")

elif (take_input == "Rock" and computer_choice == "Scissors") or \
     (take_input == "Paper" and computer_choice == "Rock") or \
     (take_input == "Scissors" and computer_choice == "Paper"):
    print("You win")

else:
    print("You lose")