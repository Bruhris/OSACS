# Boris Wang
# Exercise 3 - Functions in Python
# Computer Science 20, blk 3
# March 10, 2021

# This program is my own work - BW

import random

def show_rules():
    print("*** Rock-Paper-Scissors ***\n")
    print('Rules:   Each player chooses either rock, paper or scissors.')
    print('         The winner is determined by the following rules:')
    print('                 rock smashes scissors -> rock')
    print('                 scissors cuts paper   -> scissors wins')
    print('                 paper covers rock     -> paper wins\n')

def get_player_choice():
    choice = input('Player choice: ')
    return choice

def get_computer_choice():
    options = ['rock','paper','scissors']
    choice = random.choice(options)
    print('Computer choice:',choice)
    return choice

def declare_winner(p,c):
    if p == 'rock':
        if c == 'scissors':
            w = 'player'
        elif c == 'paper':
            w = 'computer'
        else:
            w = 'Draw'
    elif p == 'paper':
        if c == 'rock':
            w = 'player'
        elif c == 'scissors':
            w = 'computer'
        else:
            w = 'Draw'
    else:
        if c == 'paper':
            w = 'player'
        elif c == 'rock':
            w = 'computer'
        else:
            w = 'Draw'
    print('Winner:',w)



def play_game():
    show_rules()
    player = get_player_choice()
    computer = get_computer_choice()
    declare_winner(player, computer)


def main():
    play_game()


if __name__ == "__main__":
    #runs all code under main function
    main()