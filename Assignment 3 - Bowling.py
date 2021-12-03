import random

class Bowling:
    def __init__(self):
        self.score = 0

    def get_frames(self):
        while True:
            try:
                frames = input("How many frames do you want to play against the computer? ")
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
                pins = int(input("How many pins do you in your game? "))
                self.pins = pins
                break
            except TypeError:
                print("That is not a valid input!")

    def throw(self):
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
        print(f"There are {self.pins} remaining")
            
        



def main():
    print("Welcome to Boris' Bowling Game!~")
    BowlingGame = Bowling()
    BowlingGame.get_frames()
    BowlingGame.get_throws()
    BowlingGame.get_pins()

    BowlingGame.throw()

if __name__ == "__main__":
    main()