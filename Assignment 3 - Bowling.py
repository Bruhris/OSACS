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
    
    def set_players(self, players):
        self.players = players
    
    def get_players(self):
        return self.players
    
    def scoring_report(self, points, name):
        print(f"{name} now has a total of {points} points!\n")
    
    def end_report(self, playersDict):
        self.high_score = 0
        self.winners = ["PLAYER"]
        for i in playersDict:
            player = playersDict.get(i)
            print(f"{player.get_name()} end up with a total of {player.get_score()} points!")
            if player.get_score() > self.high_score:
                self.high_score = player.get_score()
                self.winner[0] = player.get_name()
            elif player.get_score() == self.high_score():
                self.winner.append(player.get_name())
        if self.winner.size() > 1:
            print(f"There was a tie between {str(self.winner)[1:-1]}!")
        else:
            print(f"The winner of the game is {self.winner}!")

        

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
        Game = BowlingGame()
        no_players = int(input("How many players will be playing in this bowling game? "))
        Game.set_players(no_players)
        players = {}

        for i in range(Game.get_players()):
            objname = f"Player_{i+1}"
            name = input(f"What is the name of player {i+1}? ")
            players[objname] = Player(name)


        while True:
            try:
                frames = int(input("How many frames do you want to play? "))
                Game.set_frames(frames)
                break
            except ValueError:
                print("That is an invalid input!")

        while True:
            try:
                throws = int(input("How many throws do you want per frame? "))
                for i in players:
                    player = players.get(i)
                    player.set_throws(throws)
                break
            except ValueError:
                print("That is an invalid input!")

        for i in range(1, Game.get_frames()+1):
            print(f"Frame: {i}")
            for player in players:
                temp = players.get(player)
                temp.throw()
                Game.scoring_report(temp.get_score(), temp.get_name())

        Game.end_report(players)
        again = play_again()
        if again == False:
            print("Thanks for playing my game!")
            break

def play_again():
    choice = input("Do you want to play again? (Y or N)").lower()
    while choice != "n" and choice != "y":
        print("That is an invalid input!")
        choice = input("Do you want to play again? (Y or N)").lower()
    if choice == "n":
        return False
    else:
        return True

if __name__ == "__main__":
    main()