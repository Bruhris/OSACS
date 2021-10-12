# * ***********************************************************************
# Boris Wang
# Exercise 1 - Leap Year
# Computer Science 30 - Block 6
# September 13, 2021

# This program is my own work - BW

import string

words_e = 0
percent = 0

base_text = "Tomorrow, and tomorrow, and tomorrow, Creeps in this petty pace from day to day, To the last syllable of recorded time; And all our yesterdays have lighted fools The way to dusty death. Out, out, brief candle! Life's but a walking shadow, a poor player, That struts and frets his hour upon the stage, And then is heard no more. It is a tale Told by an idiot, full of sound and fury, Signifying nothing."

new_text = base_text.translate(str.maketrans('', '', string.punctuation)) # Replaces all punctuation symbols with ' '

print('"'+new_text+'"')

text_words = new_text.split() # Puts all words into a list

for i in text_words:
    if 'e' in i:
        words_e += 1

num_words = len(text_words)

if words_e != 0: 
    percent = words_e/num_words * 100

print('Your text contains', num_words, 'words, of which',
      words_e, '('+str(round(percent,1))+'%) contain the letter "e".')
