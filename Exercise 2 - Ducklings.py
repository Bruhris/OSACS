"""Duckling Screensaver, by Al Sweigart al@inventwithpython.com
A screensaver of many many ducklings.
>" )   =^^)    (``=   ("=  >")    ("=
(  >)  (  ^)  (v  )  (^ )  ( >)  (v )
 ^ ^    ^ ^    ^ ^    ^^    ^^    ^^
This code is available at https://nostarch.com/big-book-small-python-programming
Tags: large, artistic, object-oriented, scrolling"""

import random, shutil, sys, time


PAUSE = 0.2
DENSITY = 0.10

DUCKLING_WIDTH = 5
LEFT = 'left'
RIGHT = 'right'
BEADY = 'beady'
WIDE = 'wide'
HAPPY = 'happy'
ALOOF = 'aloof'
CHUBBY = 'chubby'
VERY_CHUBBY = 'very chubby'
OPEN = 'open'
CLOSED = 'closed'
OUT = 'out'
DOWN = 'down'
UP = 'up'
HEAD = 'head'
BODY = 'body'
FEET = 'feet'


WIDTH = shutil.get_terminal_size()[0]

WIDTH -= 1


def main():
    print('Duckling Screensaver, by Al Sweigart')
    print('Press Ctrl-C to quit...')
    time.sleep(2)

    ducklingLanes = [None] * (WIDTH // DUCKLING_WIDTH)

    while True:  
        for laneNum, ducklingObj in enumerate(ducklingLanes): # Goes through ducklingLanes and gets the laneNum (index) and the ducklingObj (element)
            
            if (ducklingObj == None and random.random() <= DENSITY): # If element is None and a random value is less than or equal to DENSITY
                    
                    ducklingObj = Duckling()                        # Create new ducklingObj and assign it to current element
                    ducklingLanes[laneNum] = ducklingObj

            if ducklingObj != None: # If ducklingObj is not equal to none
                
                # Displays part of the duckling then selects new body part
                print(ducklingObj.getNextBodyPart(), end='')
                # If there are no more parts of the duckling to display, reassign element to none
                if ducklingObj.partToDisplayNext == None:
                    ducklingLanes[laneNum] = None
            else:
                print(' ' * DUCKLING_WIDTH, end='') # If the ducklingObj is none and random value is more then DENSITY, finishing drawing the current duck

        print()  
        sys.stdout.flush() 
        time.sleep(PAUSE)

# Create Duckling class
class Duckling:
    # Constructor of Duckling that gives random attributes to new duckling
    def __init__(self):
        # Assigns a random attributes to duckling
        self.direction = random.choice([LEFT, RIGHT])
        self.body = random.choice([CHUBBY, VERY_CHUBBY])
        self.mouth = random.choice([OPEN, CLOSED])
        self.wing = random.choice([OUT, UP, DOWN])
        
        if self.body == CHUBBY:
            self.eyes = BEADY
        else:
            self.eyes = random.choice([BEADY, WIDE, HAPPY, ALOOF])
        # First part to display is HEAD
        self.partToDisplayNext = HEAD

    # Creates head duckling as string based on instance variables and returns string
    def getHeadStr(self):
        headStr = ''
        if self.direction == LEFT:

            if self.mouth == OPEN:
                headStr += '>'
            elif self.mouth == CLOSED:
                headStr += '='


            if self.eyes == BEADY and self.body == CHUBBY:
                headStr += '"'
            elif self.eyes == BEADY and self.body == VERY_CHUBBY:
                headStr += '" '
            elif self.eyes == WIDE:
                headStr += "''"
            elif self.eyes == HAPPY:
                headStr += '^^'
            elif self.eyes == ALOOF:
                headStr += '``'

            headStr += ') ' 

        if self.direction == RIGHT:
            headStr += ' ('  

            if self.eyes == BEADY and self.body == CHUBBY:
                headStr += '"'
            elif self.eyes == BEADY and self.body == VERY_CHUBBY:
                headStr += ' "'
            elif self.eyes == WIDE:
                headStr += "''"
            elif self.eyes == HAPPY:
                headStr += '^^'
            elif self.eyes == ALOOF:
                headStr += '``'

            # Get the mouth:
            if self.mouth == OPEN:
                headStr += '<'
            elif self.mouth == CLOSED:
                headStr += '='

        if self.body == CHUBBY:

            headStr += ' '

        return headStr

    # Creates body of duckling as string based on instance variables and returns string
    def getBodyStr(self):
        bodyStr = '('  
        if self.direction == LEFT:
            if self.body == CHUBBY:
                bodyStr += ' '
            elif self.body == VERY_CHUBBY:
                bodyStr += '  '

            if self.wing == OUT:
                bodyStr += '>'
            elif self.wing == UP:
                bodyStr += '^'
            elif self.wing == DOWN:
                bodyStr += 'v'

        if self.direction == RIGHT:

            if self.wing == OUT:
                bodyStr += '<'
            elif self.wing == UP:
                bodyStr += '^'
            elif self.wing == DOWN:
                bodyStr += 'v'

            if self.body == CHUBBY:
                bodyStr += ' '
            elif self.body == VERY_CHUBBY:
                bodyStr += '  '

        bodyStr += ')'

        if self.body == CHUBBY:
            bodyStr += ' '

        return bodyStr
    # Creates feet of duckling as string based on instance variables and returns it
    def getFeetStr(self):
        if self.body == CHUBBY:
            return ' ^^  '
        elif self.body == VERY_CHUBBY:
            return ' ^ ^ '

    # Checks which body part must be displayed next and returns the body part. If there is nobody parts left, return none
    def getNextBodyPart(self):
        if self.partToDisplayNext == HEAD: # If displayed HEAD already, display BODY next
            self.partToDisplayNext = BODY
            return self.getHeadStr()    
        elif self.partToDisplayNext == BODY: # If displayed BODY already, display FEET next
            self.partToDisplayNext = FEET
            return self.getBodyStr()
        elif self.partToDisplayNext == FEET: # If displayed FEET already, no more to display so return NONE
            self.partToDisplayNext = None
            return self.getFeetStr()



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # When Ctrl-C is pressed, end the program.