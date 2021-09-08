import string

words_e = 0
percent = 0

base_text = input("Enter the text you want analyzed: ")

new_text = base_text.translate(str.maketrans('', '', string.punctuation))

text_words = new_text.split()

for i in text_words:
    if 'e' in i:
        words_e += 1

num_words = len(text_words)

if words_e != 0:
    percent = words_e/num_words * 100

print('Your text contains', num_words,'of which',words_e,'('+str(percent)+'%) contain an "e".')

