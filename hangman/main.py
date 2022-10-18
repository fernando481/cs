import re

# Get the answer. 
answer = "what's up, Doc?"

answer = answer.upper()

# pre-game setup.
answer_guessed = []

for current_answer_character in answer:
    if re.search("^[A-Z]$", current_answer_character):
        answer_guessed.append(False)
    else:
        answer_guessed.append(True)

# Game Logic.
num_of_incorrect_guesses =  5

current_incorrect_guesses = 0

Letters_guessed = {}

# User gameplay.
while current_incorrect_guesses < num_of_incorrect_guesses and False in answer_guessed:
    # Display game summary.
    print(f"number of incorrect guesses remaining: {num_of_incorrect_guesses - current_incorrect_guesses}")