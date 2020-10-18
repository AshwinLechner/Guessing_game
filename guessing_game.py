"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random


def start_game():



# Kick off the program by calling the start_game function.
    start_game()


try:
    def numberGuessed(num):
        num = int(num)
        return num

    
    print("""
    Welcome to the guessing game!
    Please guess a number between 1 and 10
    """)

    random_number = random.randint(1, 10)
    
    number_guessed = numberGuessed(input())
    
    number_of_tries = 1

    while True:
        if number_guessed == random_number:
            print("Thats correct! i took you {} tries to guess the correct number.".format(number_of_tries))
            break
        elif number_guessed > random_number:
            print("the number is lower.  ")
            number_guessed = numberGuessed(input("please try again "))
            number_of_tries += 1
            continue
        elif number_guessed < random_number:
            print("the number is higher.  ")
            number_guessed = numberGuessed(input("please try again "))
            number_of_tries += 1
            continue
    
except ValueError:
    print("please select a valid number")
    
print("The game is over now, thank you for playing")    

