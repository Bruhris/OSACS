# * ***********************************************************************
# Boris Wang
# Assignment 2 - Bowling
# Computer Science 30 - Block 6
# December 17, 2021

# This program is my own work - BW

# Import modules

import random
import time

class Player: # Initialize Player class
    def __init__(self, name): # Create constructors that takes in a name parameters and creates default values for instance variables
        self.score = 0
        self.pins = 10
        self.name = name
    
    def get_name(self): # Function to return the name of object
        return self.name
    
    def set_throws(self, throws): # Function that takes in a parameters and sets it to the number of throws that the player has
        self.throws = throws

    def get_score(self): # Functions that returns the score of the player
        return self.score

    def throw(self): # Functions when the user throws the bowling ball
        for i in range(self.throws): # For every throw
            self.bowl = random.choice(["hit", "hit", "hit", "miss"]) # Random chance of not hitting the pins
            if self.bowl == "hit": # If you hit the pins, random number of pins are hit and remain pins are calculated
                self.hit_pins = random.randint(1, self.pins)
                print(f"On throw {i+1}, {self.name} hit {self.hit_pins} pin(s)!")
                time.sleep(0.5)
                self.pins = self.pins - self.hit_pins
            else:
                print(f"OH NO! {self.name} missed and hit 0 pins!") # If you miss, custom message and you hit 0 pins
                time.sleep(0.5)

            if self.pins == 0 and i + 1 == 1:
                print(f"{self.name} hit a flush and gained 20 points!") # If you hit a flush, give the player 20 points
                self.score += 20
                time.sleep(0.5)
                break

            elif self.pins == 0 and i + 1 == 2:
                print(f"{self.name} hit a spare and gained 15 points!") # If you hit a spare, give the player 15 points
                self.score += 15
                time.sleep(0.5)
                break

            elif self.pins == 0: # If all the pins are hit, give player 10 points
                self.score += 10
                break

        if self.pins != 0:
            self.score += 10 - self.pins # If not all pins are hit, add one point to player score for each pin hit
        
        self.pins = 10 # Reset number of pins after each throw



class BowlingGame:
    def __init__(self): # Blank constructor
        pass

    def set_frames(self, frames): # Set the frames of the bowling game
        self.frames = frames

    def get_frames(self): # Return the frames of the bowling game
        return self.frames
    
    def set_players(self, players): # Set the players that will be in the game
        self.players = players
    
    def get_players(self): # Return number of players in the game
        return self.players
    
    def round_display(self, points, name): # Displays the score of a player after every round
        print(f"{name} now has a total of {points} points!")
        time.sleep(0.5)
        print()
    
    def end_report(self, playersDict): # Displays the ending score between the players and who won the bowling game
        self.high_score = 0
        self.winners = ["PLAYER"]
        for i in playersDict: # Gets the dictionary containing all player objects and checks their score
            self.player = playersDict.get(i)
            print(f"{self.player.get_name()} ended up with a total of {self.player.get_score()} points!")
            if self.player.get_score() > self.high_score: # If the current score is higher than the high score, make new high score current score
                self.winners = ["PLAYER"]
                self.high_score = self.player.get_score()
                self.winners[0] = self.player.get_name() # Assign the first element of the winner list to the name of the player with the new high score
            elif self.player.get_score() == self.high_score: # If there is a tie, add both names to winner list
                self.winners.append(self.player.get_name())
        if "PLAYER" in self.winners: # In the case where the highest score is 0, remove placeholder element in winners list
            self.winners.remove("PLAYER")
            time.sleep(0.5)
        if len(self.winners) > 1: # If there is a tie, list off the players in the winner list and the score
            print(f"There was a tie between the players:", end=" ")
            print(*self.winners, sep=', ', end='')
            print(f" with a score of {self.high_score}! Congratulations, you are all #1 bowlers!")
        else: # If there is a winner, list the name of the winning player in the list and the score
            print(f"The winner of the game is {str(self.winners[0])} with a score of {self.high_score}! Congratulations, you are the #1 bowler!")
        time.sleep(0.5)
    

def play_again(): # Check to see if user wants to play the bowling game again
    while True:
        choice = input("Do you want to play again? (Y or N) ").lower()
        if choice != "n" and choice != "y":
            print("That is an invalid input!")
            continue
        else:
            break 
        
    if choice == "n":
        return False
    else:
        return True

        

def main(): # Basic rules and instructions for how to use the bowling program
    print("Welcome to Boris' Bowling Game!~")
    time.sleep(0.7)
    print("The rules of Bowling are shown below:")
    time.sleep(0.6)
    print("- The goal is to knock down all ten pins")
    time.sleep(0.5)
    print("- Each game will have a certain number of frame and each frame will consist of a number of throws")
    time.sleep(0.5)
    print("- There will be two players and each will have an individual score, with the winner having the highest score by the last frame")
    time.sleep(0.5)
    print("- If all pins are knocked over in the first throw of a frame, it will be counted as a STRIKE and you will gain 20 points")
    time.sleep(0.5)
    print("- If all pins are knocked over in the second throw of a frame, it will be counted as a SPARE and you will gain 15 points")
    time.sleep(0.5)
    print("- Each pin knocked over will be counted as 1 point if all ten pins are not knocked over or if all pins are not all knocked over within the first two frames")
    
    while True: # Main game loop
        Game = BowlingGame() # Instantiate BowlingGame class as Game
        while True: # Error-checking to find how many players will be in the game
            try:
                no_players = int(input("How many players will be playing in this bowling game? "))
            except ValueError:
                print("That is an invalid input!")
                continue
            else:
                break
     
        Game.set_players(no_players) # Sets the number of players to BowlingGame object instance variable
        players = {}

        for i in range(Game.get_players()): # Creates a dictionary of Player objects with a name inputted from the user for each Player using # of players in the BowlingGame object
            objname = f"Player_{i+1}"
            name = input(f"What is the name of player {i+1}? ")
            players[objname] = Player(name) # Instantiate Player class with a name as a parameter and add it to dictionary for every player in game


        while True: # Error-checking to set the number of frames that will be played to BowlingGame object instance variable
            try:
                frames = int(input("How many frames do you want to play? "))
                Game.set_frames(frames)
                break
            except ValueError:
                print("That is an invalid input!")

        while True: # Error-checking to set the number of throws that the player will throw in each frame to each Player object in players dictionary
            try:
                throws = int(input("How many throws do you want per frame? "))
                for i in players:
                    player = players.get(i)
                    player.set_throws(throws)
            except ValueError:
                print("That is an invalid input!")
                continue
            else:
                break
        time.sleep(0.5)
        for i in range(1, Game.get_frames()+1): # Prints the results of each frame and how each frame goes for each user
            print(f"Frame: {i}")
            time.sleep(0.5)
            for player in players:
                temp = players.get(player) # Get the player object from dictionary and set it as variable temp
                temp.throw() # Run the throw function on object
                Game.round_display(temp.get_score(), temp.get_name()) # Run the round display using a player object
                time.sleep(0.5)

        Game.end_report(players) # Reports the end of the game and who wins the bowling game
        print()
        time.sleep(0.5)
        again = play_again() # Asks the user if they want to play the game again
        if again == False: # If no, stop game, otherwise resets loop and recreates BowlingGame and Player objects
            print("Thanks for playing my game!")
            break

if __name__ == "__main__": # Runs the main function with the game loop
    main()