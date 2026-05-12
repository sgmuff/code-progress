import random # Importing the random module to select a random word from the list

# Stages of the hangman, from full hangman to no hangman, represented as ASCII art
stages = [r"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
""", r"""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""", r"""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
""", r"""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
""", r"""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
""", r"""
  +---+
  |   |
  O   |
      |
      |
      |
=========
""", r"""
  +---+
  |   |
      |
      |
      |
      |
=========
"""]

word_list = ["aardvark", "baboon", "camel"] # List of possible words for the hangman game
chosen_word = random.choice(word_list) # Randomly selecting a word from the list to be the word to guess

display = ["_"] * len(chosen_word) # Creating a display list that will show the correctly guessed letters and underscores for the remaining letters

guessed_letters = set() # A set to keep track of the letters that have already been guessed by the player, to prevent duplicate guesses
lives = 6 # The number of lives the player has, which corresponds to the stages of the hangman. The player loses a life for each incorrect guess.

print("Welcome to Hangman!") # Greeting the player and starting the game

while lives > 0 and "_" in display: # The game continues until the player runs out of lives or successfully guesses the word

    print("\nWord:", " ".join(display)) # Displaying the current state of the word with guessed letters and underscores
    print(f"Guessed letters: {' '.join(sorted(guessed_letters))}") # Displaying the letters that have already been guessed by the player, sorted alphabetically for better readability

    guess = input("Guess a letter: ").lower() # Prompting the player to input a letter as their guess, and converting it to lowercase to ensure consistency in comparisons

    # Already guessed check
    if guess in guessed_letters: # Checking if the guessed letter has already been guessed before
        print(f"You already guessed '{guess}'. Try another letter.") # Informing the player that they have already guessed that letter and prompting them to try a different one
        continue # If the letter has already been guessed, skip the rest of the loop and prompt for another guess

    guessed_letters.add(guess) # Adding the guessed letter to the set of guessed letters to keep track of it for future checks

    # Correct guess handling
    if guess in chosen_word: # Checking if the guessed letter is in the chosen word
        for i, letter in enumerate(chosen_word): # Looping through each letter in the chosen word to find all occurrences of the guessed letter
            if letter == guess: # If the current letter in the chosen word matches the guessed letter, update the display list at the corresponding index to show the correctly guessed letter
                display[i] = letter # Updating the display list to reveal the correctly guessed letter in its correct position(s)
        print("Good guess!") # Informing the player that their guess was correct

    else: # If the guessed letter is not in the chosen word, the player loses a life
        lives -= 1 # Decreasing the number of lives by 1 for an incorrect guess
        print(f"Wrong guess! You lose a life.") # Informing the player that their guess was incorrect and that they have lost a life

    print(stages[lives]) # Displaying the current stage of the hangman based on the number of lives remaining, which visually represents how close the player is to losing the game

# End game result
if "_" not in display: # If there are no underscores left in the display list, it means the player has successfully guessed all the letters in the word and wins the game
    print("\nYou win! 🎉 The word was:", chosen_word)
else:
    print("\nYou lose! 💀 The word was:", chosen_word)