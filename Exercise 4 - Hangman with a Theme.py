# * ***********************************************************************
# Boris Wang
# Exercise 1 - Leap Year
# Computer Science 30 - Block 6
# September 16, 2021

# This program is my own work - BW

import random
import time

def display_game(missed_letters, correct_letters, secret_word):

    print('Missed letters:', end=' ')
    for letter in missed_letters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secret_word)

    for i in range (len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks [:i] + secret_word[i] + blanks [i+1:]
    for letter in blanks:
        print(letter, end=' ')
    print()

def get_guess (already_guessed):
    while True:
        guess = input('Guess a letter: ')
        guess = guess.lower()
        if len(guess) != 1:
            print('You entered more than one letter!')
        elif guess in already_guessed:
            print('You have already guessed that letter! Try again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Hey! That is not a letter!')
        else:
            return guess

def main():
    secret_words = ['apple', 'orange', 'strawberry', 'banana', 'watermelon', 'peach']
    secret_word = random.choice(secret_words)
    missed_letter_count = len(secret_word)
    missed_letters = ''
    correct_letters = ''
    game_is_done = False

    print("Welcome to Boris' Hangman Game!")
    time.sleep(2)
    print("The theme of this hangman is: Fruit!")
    time.sleep(2)
    print("Lets try guessing this word!")
    time.sleep(1)

    while True:
        display_game(missed_letters, correct_letters, secret_word)
        guess = get_guess(missed_letters + correct_letters)

        if guess in secret_word:
            correct_letters = correct_letters + guess

            found_all_letters = True
            for i in range (len(secret_word)):
                if secret_word[i] not in correct_letters:
                    found_all_letters = False
                    break
            if found_all_letters:
                print('Yes! The secret word is ' + secret_word + '"! You have won"')
                game_is_done = True

        else:
            missed_letters += guess

            if len(missed_letters) == missed_letter_count:
                display_game(missed_letters, correct_letters, secret_word)
                print('You have run out of guesses!\nAfter ' +
                    str(len(missed_letters)) + ' missed guesses and ' +
                    str(len(correct_letters)) + ' correct guesses, the word was ' + secret_word + '!')
                game_is_done = True

        if game_is_done:
            again = input("Do you want to play again? (Y or N): ") 
            while again.lower() != 'n' and again.lower() != 'y':
                print("That is an invalid option!")
                again = input("Do you want to play again? (Y or N): ") 
            if again.lower() == 'n':
                print('See you next time')
                break
            else:
                secret_words = ['apple', 'orange', 'strawberry', 'banana', 'watermelon', 'peach','blackberries','cantaloupe','cherries', 'grapes','mango','pineapple','tangerine']
                secret_word = random.choice(secret_words)
                missed_letter_count = len(secret_word)
                missed_letters = ''
                correct_letters = ''
                game_is_done = False

main()
