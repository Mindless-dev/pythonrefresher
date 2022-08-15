# rock paper scissors game

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
---'   ____)____
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


moves = [rock, paper, scissors]

computer_move = moves[random.randint(0, len(moves)-1)]

user_input = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))

user_move = moves[user_input]

print(f"computers move:\n {computer_move}")
print(f"you choose: \n {user_move}")

if user_move == rock and computer_move == paper:
    print("You win")
elif user_move == paper and computer_move == rock:
    print("You win")
elif user_move == scissors and computer_move == paper:
    print("You win")
elif user_move == computer_move:
    print("Tie, try again")
else:
    print("You lose, try again")


# alternativ løsning: bruke indecies og bruke reglene med nummer.
