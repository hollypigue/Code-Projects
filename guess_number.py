#guess the number game

import random

def guess_number():
    random_number = random.randint(1,100)
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I will think of a number between 1 and 100, can you guess it?")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < random_number:
            print("Too low, guess again: ")
        elif guess > random_number:
            print("Too high, guess again: ")
        else:
            print("Good job you guessed the number in", attempts, "attempts!")
            break

guess_number()
