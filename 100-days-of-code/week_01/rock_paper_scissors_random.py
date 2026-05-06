import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

GAME_IMAGES = [rock, paper, scissors]

# A lookup table is cleaner than a chain of if/elif for fixed relationships.
# Key = choice, value = what it beats.
WINS_AGAINST = {0: 2, 1: 0, 2: 1}  # rock beats scissors, paper beats rock, scissors beats paper

user_input = input("What do you choose? Type 1/2/3 or rock/paper/scissors.\n").lower()

# Map every valid input to a 0-based index. None signals invalid input.
if user_input == "1" or user_input == "rock":
    user_choice = 0
elif user_input == "2" or user_input == "paper":
    user_choice = 1
elif user_input == "3" or user_input == "scissors":
    user_choice = 2
else:
    user_choice = None

# Lesson: validate input before using it. The original code ran game logic
# first and checked validity afterward, which caused crashes and wrong results.
if user_choice is None:
    print("Invalid choice — you lose!")
else:
    computer_choice = random.randint(0, 2)

    print(GAME_IMAGES[user_choice])
    print("Computer chose:")
    print(GAME_IMAGES[computer_choice])

    if user_choice == computer_choice:
        print("It's a draw!")
    elif WINS_AGAINST[user_choice] == computer_choice:
        print("You win!")
    else:
        print("You lose!")