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

Letters_guessed = []

# User gameplay.
while current_incorrect_guesses < num_of_incorrect_guesses and False in answer_guessed:
    # Display game summary.
    print(f"number of incorrect guesses remaining: {num_of_incorrect_guesses - current_incorrect_guesses}")

    print("Guess letters; ", end="")

    for current_letter_guessed in Letters_guessed:
        print(current_letter_guessed, end=" ")
    
    print()

    # Display puzzle board.
    for current_answer_indix in range(len(answer)):
        if answer_guessed[current_answer_indix]:
            print(answer[current_answer_indix], end="")
        else:
            print("_", end="")
    
    print()

    # Let user guess a letter.
    letter = input("Enter a letter: ")

    letter = letter.upper()

    # cheack if user entered a valid letter.
    if re.search("^[A-Z]$",letter) and len(letter) == 1 and letter not in Letters_guessed:
        # insert the letter guessed by the user (insertion sort)
        current_letter_index = 0

        for current_letter_guessed in Letters_guessed:
            if letter < current_letter_guessed:
                break

            current_letter_index += 1
        
        Letters_guessed.insert(current_letter_index, letter)

        # cheak if letter is in the puzzle.
        if letter in answer:
            for current_answer_indix in range(len(answer)):
                if letter == answer[current_letter_index]:
                    answer_guessed[current_letter_index] = True
        else:
            current_incorrect_guesses += 1

# post game summery.
if current_incorrect_guesses < num_of_incorrect_guesses:
    print("congratulation, you won ")
else:
    print(f"sorry,loser, the answer wa {answer}")