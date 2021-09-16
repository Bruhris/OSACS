# * ***********************************************************************
# Boris Wang
# Exercise 1 - Leap Year
# Computer Science 30 - Block 6
# September 13, 2021

# This program is my own work - BW

import random

def display_game(missed_letters, correct_letters, secret_word):
    # this function prints out the missed letters and the word with blanks and letters

    print('Missed letters:', end=' ')
    for letter in missed_letters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secret_word)

    for i in range (len(secret_word)):
        # replace blanks with correctly guessed letters
        if secret_word[i] in correct_letters:
            blanks = blanks [:i] + secret_word[i] + blanks [i+1:]
    for letter in blanks:
        #show the secret work with the spaces in between each letter
        print(letter, end=' ')
    print()

def get_guess (already_guessed):
    # this function will return the letter the player enters ensuring that it is a different letter from before
    while True:
        print('Guess a letter: ')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in already_guessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def main():
    secret_words = ['apple', 'orange', 'strawberry', 'banana', 'watermelon', 'peach']
    secret_word = random.choice(secret_words)
    missed_letter_count = 7
    missed_letters = ''
    correct_letters = ''
    game_is_done = False

    print("Welcome to Boris' Hangman Game!/nThe theme of this hangman is fruit!")
    while True:
        display_game(missed_letters, correct_letters, secret_word)
        # let the player enter a letter
        guess = get_guess(missed_letters + correct_letters)

        if guess in secret_word:
            correct_letters = correct_letters + guess

            #Check if the player has won
            found_all_letters = True
            for i in range (len(secret_word)):
                if secret_word[i] not in correct_letters:
                    found_all_letters = False
                    break
            if found_all_letters:
                print('Yes! The secret word is ' + secret_word + '"! You have won"')
                game_is_done = True

        else:
            missed_letters = missed_letters + guess

            # check if the player has guessed too many times and lost

            if len(missed_letters) == missed_letter_count - 1:
                display_game(missed_letters, correct_letters, secret_word)
                print('You have run out of guesses!\nAfter ' +
                    str(len(missed_letters)) + ' missed guesses and ' +
                    str(len(correct_letters)) + ' correct guesses, the word was ' + secret_word + '!')
                game_is_done = True

        if game_is_done:
            again = input("Do you want to play again? (Y or N)") 
            if again.lower() == 'n':
                print('See you next time')
                break
            else:
                secret_words = ['apple', 'orange', 'strawberry', 'banana', 'watermelon', 'peach']
                secret_word = random.choice(secret_words)
                missed_letter_count = 7
                missed_letters = ''
                correct_letters = ''
                game_is_done = False

main()
