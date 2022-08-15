import random
from hangman_words import word_list
from hangman_art import logo, stages


print(logo)
player_lives = 6
chosen_word = random.choice(word_list)

# test
print(f'Pssst, the solution is {chosen_word}.')


display = []


for letter in chosen_word:
    display.append("_")


while "_" in display and player_lives != 0:

    print(stages[player_lives])
    print(display)

    guess_letter = input("Guess a letter: ").lower()

    for i in range(0, len(chosen_word)):
        if guess_letter == chosen_word[i]:
            display[i] = guess_letter

    if guess_letter not in chosen_word:
        player_lives = player_lives - 1
        print(f"the letter {guess_letter} is not in the word.")

    if guess_letter in display:
        print(f"you have already guessed the letter {guess_letter} :)")

    print(stages[player_lives])
    print(display)

    if "_" not in display:
        print("You Win!")
    elif player_lives == 0:
        print("Game Over!")
