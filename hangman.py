#hangman game

import random

def hangman():
    words = ['apple', 'house', 'water', 'octopus', 'photograph', 'midnight', 'lemon', 'money', 'group', 'mother']
    word = random.choice(words)
    guessed_letters = []
    tries = 6
    
    print("Welcome to Hangman!")
    print("_ " * len(word))
    
    while tries > 0:
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1:
            print("Please enter only one letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        if guess not in word:
            tries -= 1
            print("Wrong guess! Tries left:", tries)
            
            if tries == 0:
                print("You lost! The word was", word)
                break
        else:
            guessed_letters.append(guess)
            progress = ''
            for letter in word:
                if letter in guessed_letters:
                    progress += letter + ' '
                else:
                    progress += '_ '
            
            print(progress)
            
            if '_' not in progress:
                print("Congratulations! You won!")
                break

hangman()




