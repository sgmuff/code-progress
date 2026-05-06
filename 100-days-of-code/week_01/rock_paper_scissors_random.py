import random # This import is needed to use the random module for generating computer choices.

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

GAME_IMAGES = [rock, paper, scissors] # This index makes it easy to display the correct image based on the user's choice (0, 1, or 2).

# A lookup table is cleaner than a chain of if/elif for fixed relationships. AI taught me this one.
# Key = choice, value = what it beats. # A key is on the left, and the value is on the right. So 0 (rock) beats 2 (scissors), 1 (paper) beats 0 (rock), and 2 (scissors) beats 1 (paper).
WINS_AGAINST = {0: 2, 1: 0, 2: 1}  # rock beats scissors, paper beats rock, scissors beats paper

user_input = input("What do you choose? Type 1/2/3 or rock/paper/scissors.\n").lower() # The .lower() method converts the user's input to lowercase, making the input case-insensitive. This allows users to enter "Rock", "rock", "ROCK", etc., and it will still be recognized as a valid choice.

# The original code only accepted "rock", "paper", or "scissors" as valid inputs, which caused issues when users entered "1", "2", or "3". 
# This change allows for both numeric and text inputs, improving user experience and preventing crashes from invalid input.
if user_input == "1" or user_input == "rock":
    user_choice = 0
elif user_input == "2" or user_input == "paper": 
    user_choice = 1
elif user_input == "3" or user_input == "scissors":
    user_choice = 2
else:
    user_choice = None # Setting user_choice to None for invalid input allows us to check for validity before proceeding with the game logic, preventing crashes and ensuring correct results.

if user_choice is None:
    print("Invalid choice — you lose!")
else:
    computer_choice = random.randint(0, 2) # This line generates a random integer between 0 and 2 (inclusive) to represent the computer's choice of rock, paper, or scissors.

    print(GAME_IMAGES[user_choice]) # This line displays the image corresponding to the user's choice by indexing into the GAME_IMAGES list with user_choice. For example, if user_choice is 0 (rock), it will display the rock image.
    print("Computer chose:")
    print(GAME_IMAGES[computer_choice])

    if user_choice == computer_choice: # This line checks if the user's choice is the same as the computer's choice. If they are equal, it means both players chose the same option, resulting in a draw.
        print("It's a draw!")
    elif WINS_AGAINST[user_choice] == computer_choice: # This line checks if the user's choice beats the computer's choice by looking up the user's choice in the WINS_AGAINST dictionary. If the value (the choice that the user's choice beats) matches the computer's choice, it means the user wins.
        print("You win!")
    else:
        print("You lose!") # If the user's choice does not beat the computer's choice and it's not a draw, then the user loses.