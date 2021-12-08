import random

class Player:
    def __init__(self):
        self.score = 0

    '''def throw(self):
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

    def set_pins(self, pins):
        self.pins = pins



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

            
        



def main():
    print("Welcome to Boris' Bowling Game!~")
    BowlingGame = Bowling()
    BowlingGame.get_frames()
    BowlingGame.get_throws()
    BowlingGame.get_pins()
    BowlingGame.get_players()
    player_1 = Player()
    player_2 = Player()


    


if __name__ == "__main__":
    main()