# * ***********************************************************************
# Boris Wang
# Exercise 1 - Leap Year
# Computer Science 30 - Block 6
# September 13, 2021

# This program is my own work - BW

import string

words_e = 0
percent = 0

base_text = input("Enter the text you want analyzed: ")

new_text = base_text.translate(str.maketrans('', '', string.punctuation)) # Replaces all punctuation symbols with ' '

text_words = new_text.split() # Puts all words into a list

for i in text_words:
    if 'e' in i:
        words_e += 1

num_words = len(text_words)

if words_e != 0: 
    percent = words_e/num_words * 100

print('Your text contains', num_words, 'of which',
      words_e, '('+str(percent)+'%) contain the letter "e".')
