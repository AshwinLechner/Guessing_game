"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random


def start_game():

    print("""
    Welcome to the guessing game!
    Please guess a number between 1 and 10
    """)

    def numbers_guessed():
        while True:
            try:
                guess = input(
                    "Guess a number between 1 and 10 ")
                guess = int(guess)
                break
            except ValueError:
                print("Please enter a valid number. ")
        return guess

    random_number = random.randint(1, 10)
    guessed = numbers_guessed()
    number_of_tries = 1

    while True:
        if guessed == random_number:
            print("Thats correct! i took you {} tries to guess the correct number.".format(
                number_of_tries))
            print("The game is over now, thank you for playing")
            break
        elif guessed > random_number:
            print("the number is lower.  ")
            guessed = numbers_guessed()
            number_of_tries += 1
            continue
        elif guessed < random_number:
            print("the number is higher.  ")
            guessed = numbers_guessed()
            number_of_tries += 1
            continue


start_game()
