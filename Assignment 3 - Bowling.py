import random

class Player:
    def __init__(self, name):
        self.score = 0
        self.pins = 10
        self.name = name
    
    def get_name(self):
        return self.name
    
    def set_throws(self, throws):
        self.throws = throws

    def get_score(self):
        return self.score

    def throw(self):
        for i in range(self.throws):
            self.bowl = random.choice(["hit","miss"])
            if self.bowl == "hit":
                self.hit_pins = random.randint(1, self.pins)
                print(f"On throw {i+1}, {self.name} hit {self.hit_pins} pins!")
                self.pins = self.pins - self.hit_pins
            else:
                print(f"OH NO! {self.name} missed and hit 0 pins!")

            if self.pins == 0 and i + 1 == 1:
                print(f"{self.name} hit a flush and gained 20 points!")
                self.score += 20
                break

            elif self.pins == 0 and i + 2 == 2:
                print(f"{self.name} hit a spare and gained 15 points!")
                self.score += 15

            elif self.pins == 0:
                self.score += 10
                break

        if self.pins != 0:
            self.score += 10 - self.pins
        
        self.pins = 10



class BowlingGame:
    def __init__(self):
        pass

    def set_frames(self, frames):
        self.frames = frames

    def get_frames(self):
        return self.frames
    
    def scoring_report(self, points, name):
        print(f"{name} now has a total of {points} points!")
    
    def end_report(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

        print(f"{self.player1.get_name()} ended the game with a total of {player1.get_score()}")
        print(f"{self.player2.get_name()} ended the game with a total of {player2.get_score()}")
        if self.player1.get_score() > self.player2.get_score():
            print(f"{self.player1.get_name()} has won the game by {self.player1.get_score() - self.player2.get_score()} points!")
        else:
            print(f"{self.player2.get_name()} has won the game by {self.player2.get_score() - self.player1.get_score()} points!")

def main():
    print("Welcome to Boris' Bowling Game!~")
    print("The rules of Bowling are shown below:")
    print("Rules:")
    print("- The goal is to knock down all ten pins")
    print("- Each game will have a certain number of frame and each frame will consist of a number of throws")
    print("- There will be two players and each will have an individual score, with the winner having the highest score by the last frame")
    print("- If all pins are knocked over in the first throw of a frame, it will be counted as a STRIKE and you will gain 20 points")
    print("- If all pins are knocked over in the second throw of a frame, it will be counted as a SPARE and you will gain 15 points")
    print("- Each pin knocked over will be counted as 1 point if all ten pins are not knocked over or if all pins are not all knocked over within the first two frames")
    while True:
        name1 = input("What is the name of player 1? ")
        name2 = input("What is the name of player 2? ")
        Game = BowlingGame()
        player1 = Player(name1)
        player2 = Player(name2)
        players = [player1, player2]
        print(players[0])
        frames = int(input("How many frames do you want to play? "))
        Game.set_frames(frames)
        throws = int(input("How many throws do you want per frame? "))
        for i in players:
            i.set_throws(throws)
        for i in range(1, Game.get_frames()+1):
            print(f"Frame: {i}")
            player1.throw()
            Game.scoring_report(player1.get_score(), player1.get_name())
            player2.throw()
            Game.scoring_report(player2.get_score(), player2.get_name())
        Game.end_report(player1, player2)
        again = play_again()
        if again == False:
            print("Thanks for playing my game!")
            break

def play_again():
    choice = ("Do you want to play again?").lower()
    while choice != "n" and choice != "y":
        print("That is an invalid input!")
        choice = ("Do you want to play again?").lower()
    if choice == "n":
        return False
    else:
        return True

if __name__ == "__main__":
    main()