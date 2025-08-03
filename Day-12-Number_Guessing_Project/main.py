# from artz import logo
# import random
#
# print(logo)
# randoo = random.randint(1,100)
#
# print("Welcome to the Number Guessing Game!\n")
# print("I'm thinking of a number between 1 and 100.\n")

# diff = input("Choose the difficulty. Type 'Easy' or 'Hard':").lower()
# if diff == "easy":
#     print("You have 10 attempts remaining to guess the number.\n")
#     lives=10
# else:
#     print("You have 5 attempts remaining to guess the number.\n")
#     lives=5
# game_over= False

# while not game_over:
#     guess = int(input("Make a guess:"))
#     if guess == randoo:
#         print(f"Congrats you have guessed the number, {randoo}!")
#         game_over=True
#     elif guess > randoo:
#         print("Too High\nGuess Again")
#         lives+=-1
#         print(f"You have {lives} attempts remaining to guess the number.\n")
#     elif randoo>guess:
#         print("Too Low\nGuess Again")
#         lives += -1
#         print(f"You have {lives} attempts remaining to guess the number.\n")
#     if lives==0:
#         game_over=True
#         print(f"The number was {randoo}")

from artz import logo
import random

Easy_Lev_Lives = 10
Hard_Lev_Lives = 5

def choose_dif():
    diff = input("Choose the difficulty. Type 'Easy' or 'Hard':").lower()
    if diff == "easy":
        return Easy_Lev_Lives
    else:
        return Hard_Lev_Lives


def choice(guess,randoo,lives):
        if guess > randoo:
            print("Too High\nGuess Again")
            return lives - 1
        elif randoo > guess:
            print("Too Low\nGuess Again")
            return lives - 1
        else:
            print(f"Congrats you have guessed the number, {randoo}!")


def game():

    print(logo)
    randoo = random.randint(1, 100)

    print("Welcome to the Number Guessing Game!\n")
    print("I'm thinking of a number between 1 and 100.\n")
    turns=choose_dif()
    while guess!= randoo:
        print(f"You have {turns} attempts left!")
        guess = int(input("Make a guess:"))
        turns=choice(guess,randoo,turns)
    if turns == 0:
        print(f"You lose, The number was {randoo}")
        return

game()
