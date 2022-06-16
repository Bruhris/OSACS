# * ***********************************************************************
# Boris Wang
# Assignment 3 - Medieval Battle
# Computer Science 30 - Block 6
# June 16, 2022

# This program is my own work - BW

import random
import time

class Character:
    def __init__(self, health, attack): # Initialize charcter class with variables
        self.cardName = ""
        self.health = health # Number of health points
        self.attack = attack # Amount of damage that the character can do
        self.has_casted = False # If characters ability has casted or not
        self.isallied = False  # If the charcter is allied with a healer or not

    def getName(self): # Method to retrieve name of character
        return self.cardName
    
    def getHealth(self):
        return self.health

    def is_alive(self): # Checks if the character has greater than 0 health and is still alive
        if self.health <= 0:
            return False
        return True
    
    def takeDamage(self, damage, name): # Character will take another characters attack and have their health reduced
        self.health -= damage
        damageLines = [f"{name} was hit and took {int(damage)} damage!", f"HOLY MOLY! {name} got DUNKED on and was dealt {int(damage)} damage!",
        f"CRITICAL HIT! {name} was hit for a MASSIVE {int(damage)} damage!", f"{name} got out maneuvered and recieved {int(damage)} damage!", 
        f"Shing* Shing* Shing* {name} was cut and is took {int(damage)} damage!", f"Look at the moves look at the plays! WHAT WAS THAT! {name} just took {int(damage)} damage!"]
        print(random.choice(damageLines)) # Outputs amount damage that character took, with special lines

# Human characters

class Knight(Character): # Basic character that inherits from charcter class
    def __init__(self, h, a):
        super().__init__(h, a) # Access to parents attributes and methods  
        self.cardName = "Knight" # Rename cardname attribute
    
    def ability(self, n, team, enemy):
        print(f"The knight rallies with his allies, gaining {int((n/10)*(self.attack))} attack!")
        self.attack += (n/10)*(self.attack) # Adds percentage of attack to current attack based on how many units are still on his team
        self.has_casted = True

class Crusader(Character): # Tank
    def __init__(self, h, a):
        super().__init__(h, a)
        self.defense = 5 # Special defense trait that reduces amount of damage taken
        self.cardName = "Crusader"
    
    def ability(self, n, team, enemy):
        print(f"The crusader fortifies his armor, gaining 5 more defense!")
        self.defense += 5 # Adds 5 to defense to take less damage
        self.has_casted = True
    
    def takeDamage(self, damage, name): # Method Override to account for Crusader defense
        self.health -= damage - self.defense
        print(f"The Crusader shielded himself and took {int(damage - self.defense)} damage!")

class Elf(Character): # Special
    def __init__(self, h, a):
        super().__init__(h, a)
        self.cardName = "Elf"
    
    def ability(self, n, team, enemy): # Does damage to every single unit on the enemies team
        print(f"The elf calls an arrow storm, dealing {self.attack} to every unit on the enemies team!")
        for i in team:
            i.health -= self.attack
        self.has_casted = True

class Mage(Character): # Special
    def __init__(self, h, a):
        super().__init__(h, a)
        self.cardName = "Mage"
    
    def ability(self, n, team, enemy): # Does a random amount of damage to the enemy the charater is currently facing
        damage = random.randint(1,30)
        print(f"The mage casts a spell and hits the {team[0].getName()}, dealing {damage} damage!")
        enemy.health -= damage
        self.has_casted = True

# Monsters Characters

class Goblin(Character):# Basic
    def __init__(self, h, a):
        
        super().__init__(h, a)
        self.cardName = "Goblin"
    
    def ability(self, n, team, enemy): # Increases his attack based on the number of units remaining on his team
        print(f"The goblin decieves the {team[0].getName()}, gaining {int((5-n)*0.2*(self.attack))} attack!")
        self.attack += (5-n)*0.2*(self.attack)
        self.has_casted = True

class Ogre(Character): # Tank
    def __init__(self, h, a):
        
        super().__init__(h, a)
        self.cardName = "Ogre"
    
    def ability(self, n, team, enemy): # Gains more health
        print(f"The ogre is enraged! He has gained 25 extra health!")
        self.health += 25
        self.has_casted = True

class Shaman(Character): # Special
    def __init__(self, h, a):
        
        super().__init__(h, a)
        self.cardName = "Shaman"
    
    def ability(self, n, team, enemy): # Deals 20 damage to a random member on the enemies team
        number = random.randint(0,len(team)-1)
        print(f"The shaman curses the {team[number].getName()} on the enemy team, dealing 20 damage to him!")
        team[number].health -= 20
        self.has_casted = True

class Vampire(Character): # Special
    def __init__(self, h, a):
        
        super().__init__(h, a)
        self.cardName = "Vampire"
    
    def ability(self, n, team, enemy): # Heals himself for 10 health, increases his attack by 10 and attacks the enemy for his attack amount
        print(f"The vampire sucks the blood from {team[0].getName()}, increasing his damage and health by 10 and dealing {self.attack} damage!")
        self.health += 10
        self.attack += 10
        enemy.health -= self.attack
        self.has_casted = True

class Healer(Character): # Different type of special character
    def __init__(self, h, a):
        super().__init__(h, a)
        self.cardName = "Healer"
    
    def allign(self, characters): # Ties healer with another character
        print(f"Select a character to ally your healer with: ") # Allows user to select what character to tie healer to
        for k, p in enumerate(characters): # Outputs list of characters on team
            if not isinstance(p, Healer):
                print(f"{k+1}. "+p.getName())
        ally = input() # User input and error check
        while ally.isdigit() == False or int(ally) > 3 or int(ally) <= 0 or isinstance(characters[int(ally)-1], Healer) == True:
            print("That is an invalid response, please try again")
            ally = input()
        ally = int(ally)-1
        print(f"Your healer is now allied with {characters[ally].getName()}\n") # Notifies user and makes them allied with other character object
        characters[ally].isallied = True
        time.sleep(1)

    def heal(self, character): # Heals the character for 5 health after the character attacks
        print(f"{character.getName()} is allied with a healer and healed back 5+ health points!")
        character.health += 2

class Game:
    def __init__(self):
        # Initalize character objects and roster lists
        self.knight = Knight(100, 20)
        self.crusader = Crusader(125, 10)
        self.elf = Elf(75, 25)
        self.mage = Mage(65, 23)

        self.goblin = Goblin(95, 22)
        self.ogre = Ogre(200, 13)
        self.shaman = Shaman(70, 22)
        self.vampire = Vampire(80, 25)

        self.healer = Healer(50, 0)

        self.player_turn = True
        self.has_healer = False

        self.humans = [self.knight, self.crusader, self.elf, self.mage, self.healer]
        self.monsters = [self.goblin, self.ogre, self.shaman, self.vampire, self.healer]

        # Empty player and computer roster to select characters from
        self.playerRoster = []
        self.computerRoster = []
    
    def selection(self): # User selects which side and what characters
        side = input("Would you like to be part of the Human team or Monster team (H or M)? ")
        while side.lower() != "h" and side.lower() != "m":
            print("That is an invalid response!")
            side = input("Would you like to be part of the Human team or Monster team? (H or M) ")

        if side.lower() == "h": # If the user selects the human side

            for i in range(4,0,-1): # Lists all the characters from human side and user selects from them 
                print(f"Select a card from the list using the number associated (Remaining: {i}): ")
                for k, p in enumerate(self.humans):
                    print(f"{k+1}. "+p.getName())
                selected_card = input()
                
                while selected_card.isdigit() == False or int(selected_card) > i+1 or int(selected_card) <= 0:
                    print("That is an invalid response, please try again")
                    selected_card = input()
                selected_card = int(selected_card)

                if isinstance(self.humans[selected_card-1], Healer): # Checks if the user selected healer and if they did, make the has_healer state True
                    self.has_healer = True
                else:
                    self.playerRoster.append(self.humans[selected_card-1]) # Add character to player roster if not healer
                
                self.humans.remove(self.humans[selected_card-1]) # Remove added character from human roster so no repeats
                print()

            if self.has_healer == True: # If the player has a healer, allow the user to choose who to allign the healer with
                self.healer.allign(self.playerRoster)

            self.computerRoster = self.monsters # Make the computer roster the monster roster and remove a character
            self.computerRoster.remove(random.choice(self.computerRoster)) # Remove a random character from the computer roster since max of 4 units
            random.shuffle(self.computerRoster) # Shuffle the order of characters
            for i in self.computerRoster: # Check if computer has a healer on time
                if isinstance(i, Healer):
                    self.computerRoster.remove(i) # Remove healer
                    choose = random.randint(0,len(self.computerRoster)-1) # Choose random character to ally healer to that is not a healer themselves
                    while isinstance(self.computerRoster[choose], Healer):
                        choose = random.choice(self.computerRoster)
                    self.computerRoster[choose].isallied = True
                    break
            
        
        else: # Same process as other side, but made for if the user selects the monsters side
            for i in range(4,0,-1):
                print(f"Select a card from the list using the number associated (Remaining: {i}): ")
                for k, p in enumerate(self.monsters):
                    print(f"{k+1}. "+p.getName())
                selected_card = input()

                while selected_card.isdigit() == False or int(selected_card) > i+1 or int(selected_card) <= 0:
                    print("That is an invalid response, please try again")
                    selected_card = input()
                selected_card = int(selected_card)

                if isinstance(self.monsters[selected_card-1], Healer):
                    self.has_healer = True
                else:
                    self.playerRoster.append(self.monsters[selected_card-1])
                
                self.monsters.remove(self.monsters[selected_card-1])
                print()

            if self.has_healer == True:
                self.healer.allign(self.playerRoster)
            
            self.computerRoster = self.humans
            self.computerRoster.remove(random.choice(self.computerRoster))
            random.shuffle(self.computerRoster)
            for i in self.computerRoster:
                if isinstance(i, Healer):
                    self.computerRoster.remove(i)
                    choose = random.randint(0,len(self.computerRoster)-1)
                    while isinstance(self.computerRoster[choose], Healer):
                        choose = random.choice(self.computerRoster)
                    self.computerRoster[choose].isallied = True
                    break

        
    def fight(self, player, computer): # When the computer and player characters fight
        ability_chance = [True, False] # Has a chance for either character to activate their ability during the fight
        while True: # Fight continues until one of the characters is eliminated (health has reached zero)
            if self.player_turn == True: # If it is the players turn
                if random.choice(ability_chance) and player.has_casted == False: # Check if they are able to do activate their ability and they haven't casted it already
                    print(f"{player.getName()} activated their ability!")
                    time.sleep(0.5)
                    player.ability(len(self.playerRoster), self.computerRoster, computer) # Activate ability with appropriate parameters
                    time.sleep(0.5)

                computer.takeDamage(player.attack, computer.getName()) # Computer enemy will take damage

                if player.isallied == True: # If the player is allied, they heal 5 hp after attacking
                    self.healer.heal(player)
                self.player_turn = False # Players turn is over, computers turn
                time.sleep(0.5)

                if not computer.is_alive(): # If the computer card died, alert user and return False
                    print(f"{computer.getName()} was eliminated")
                    time.sleep(0.5)
                    return False
            else:
                if random.choice(ability_chance) and computer.has_casted == False: # Check if computer card can activate their ability
                    print(f"{computer.getName()} activated their ability!")
                    time.sleep(0.5)
                    computer.ability(len(self.computerRoster), self.playerRoster, player)
                    time.sleep(0.5)

                player.takeDamage(computer.attack, player.getName()) # Player card takes damage

                if computer.isallied == True: # If computer allied, heal
                    self.healer.heal(computer)
                self.player_turn = True # Back to players turn
                time.sleep(0.5)

                if not player.is_alive(): # If player card dies, alert user and return False
                    print(f"{player.getName()} was eliminated")
                    time.sleep(0.5)
                    return False
    
    def roundReport(self, team1, team2): # Reports the healths and status of each charcter on each players team
        if len(team1) == 0:
            print("There are no characters remaining for the player.")
        else:
            for char in team1:
                print(f"{char.getName()} has {int(char.getHealth())} remaining health")
                time.sleep(0.3)
            print()

        if len(team2) == 0:
            print("There are no characters remaining for the computer.")
        else:
            for char in team2:
                print(f"{char.getName()} has {int(char.getHealth())} remaining health")
                time.sleep(0.3)
            print()

    def reset(self): # Reset objects and parameters of characters so they can start fresh
        self.knight = Knight(100, 20)
        self.crusader = Crusader(125, 10)
        self.elf = Elf(75, 25)
        self.mage = Mage(65, 23)

        self.goblin = Goblin(95, 22)
        self.ogre = Ogre(200, 13)
        self.shaman = Shaman(70, 22)
        self.vampire = Vampire(80, 25)

        self.healer = Healer(50, 0)

        self.player_turn = True
        self.has_healer = False

        self.humans = [self.knight, self.crusader, self.elf, self.mage, self.healer]
        self.monsters = [self.goblin, self.ogre, self.shaman, self.vampire, self.healer]

        # Empty player and computer roster to select characters from
        self.playerRoster = []
        self.computerRoster = []
        
    def play(self):
        self.selection() # Let user and computer select cards and roster

        print(f"The players deck is the following: ") # Output the players deck
        for k, p in enumerate(self.playerRoster):
                    print(f"{k+1}. "+p.getName())
        print()
        time.sleep(1)

        print(f"The computers deck is the following: ") # Output the computers deck
        for k, p in enumerate(self.computerRoster):
                    print(f"{k+1}. "+p.getName())
        time.sleep(1)

        print("Let the battles begin!")
        print()
        time.sleep(0.8)

        while len(self.computerRoster) != 0 and len(self.playerRoster) != 0: # While neither player has no cards remaining
            playerCard = self.playerRoster[0] # Assign the first card of each roster to the current playing card
            computerCard = self.computerRoster[0]
            print(f"The player brings out: {playerCard.getName()}!")
            time.sleep(0.3)
            print(f"The computer brings out: {computerCard.getName()}!")
            time.sleep(0.8)
            print()
            if not self.fight(playerCard, computerCard): # When one of the characters die
                if not playerCard.is_alive(): # If the player card is dead, return False
                    self.playerRoster.remove(self.playerRoster[0])
                    print()
                elif not computerCard.is_alive(): # If the computer card is dead, return False
                    self.computerRoster.remove(self.computerRoster[0])
                    print()
            time.sleep(0.5)
            self.roundReport(self.playerRoster, self.computerRoster) # Report the status of the player and computer team
            time.sleep(1)
        
        if len(self.computerRoster) == 0: # If the player wins
            print("The player has won the Medival Battle!")
        else: # If the computer wins
            print("The computer has won the Medival Battle!") 
            
def main():
    print("Welcome to Boris' Medival Battle!")
    print("Here are the rules of the game:")
    print("- You will be given the option to pick a between the Humans and the Monster team")
    print("  - The side of humans consists of a knight, crusader, elf, and mage")
    print("  - The side of monsters consists of a goblin, ogre, shaman and vampire")
    print("  - Both sides will have access to their own healer")
    print("- After you decide a side, you will select and order a team of 4 characters from 5 characters that each have special abilities")
    print("- You will NOT be able to change your team after it is select and then you will face off against a deck created by the computer")
    print("- The players will take turns attacking each other and will be able to cast their special ability once during battle")
    print("- The units will fight between each other and the winner will be decided after the other team has no more availble characters in their deck")
    print("Good luck and have fun!")
    print()
    game = Game() # Initalize game object
    while True:
        game.play() # Play the game
        again = input("Would you like to have another Medival Battle? (Y or N) ") # Ask if the user would like to play again + error checking
        while again.lower() != "y" and again.lower() != "n":
            print("That was an invalid input!")
            again = input("Would you like to have another Medival Battle? (Y or N) ")
        if again.lower() == "y":
            game.reset() # Resets game object and loops again
        else:
            print("Thanks for playing and have a great day!") # Exits loop and ends program
            break

if __name__ == "__main__": # Runs the main function with the game loop
    main()