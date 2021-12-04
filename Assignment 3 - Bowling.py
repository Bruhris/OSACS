import random

class Player:
    def __init__(self):
        self.score = 0
        self.pins = 10


class Bowling:
    def __init__(self):
        pass

    def get_frames(self):
        while True:
            try:
                frames = input("How many frames do you want to play against your opponent(s)? ")
                self.frames = frames
                break
            except TypeError:
                print("That is not a valid input!")

    def get_throws(self):
        while True:
            try:
                throws = int(input("How many throws do you want per frame? "))
                self.throws = throws
                break
            except TypeError:
                print("That is not a valid input!")

    def get_pins(self):
        while True:
            try:
                pins = int(input("How many pins do you want in your game? "))
                self.pins = pins
                break
            except TypeError:
                print("That is not a valid input!")
    def get_players(self):
        while True:
            try:
                no_players = int(input("How many players do you want in your game? "))
                self.player_num = no_players
                break
            except TypeError:
                print("That is not a valid input!")

    def set_players(self):
        return self.player_num

    '''def throw(self, player):
        self.pins_hit = random.randint(0,self.pins)
        while self.pins_hit > self.pins:
            self.pins_hit = random.randint(0,self.pins)
        if self.pins_hit == self.pins:
            self.got_Score = 20
        self.score += self.got_Score
        self.pins -= self.pins_hit
        
        print(f"You hit {self.pins_hit} pins!")
        print(f"You scored {self.got_Score} points!")
        print(f"Your total score is {self.score}!")
        print(f"There are {self.pins} remaining")'''
            
        



def main():
    print("Welcome to Boris' Bowling Game!~")
    BowlingGame = Bowling()
    BowlingGame.get_frames()
    BowlingGame.get_throws()
    BowlingGame.get_pins()
    BowlingGame.get_players()
    players = {}

    for i in range(1, BowlingGame.set_players()+1):
        name = "player_{}".format(i)
        players[name] = players.get(name, Player())


    


if __name__ == "__main__":
    main()