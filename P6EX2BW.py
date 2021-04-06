# Boris Wang
# Exercise 2 - Palindrome
# Computer Science 20, blk 3
# April 5, 2021

# This program is my own work - BW

def palindrome(something):
    # Takes the string and reverse the string
    revSomething = something[::-1]
    return revSomething


if __name__ == "__main__":
    # Takes input from user for a potential palindrome
    string = input(
        "What string do you want to check to see if it's a palindrome? (No punctuation or symbols!)\n")
    # removes all the spaces from string and makes all cases lower
    ok = string.replace(' ', "")
    ok = ok.lower()
    # puts string into palindrome function
    reverseString = palindrome(ok)
    # if the default string is the same as the reversed string or not, then it will print a specific message
    if ok == reverseString:
        print('WOW! "' + string + '" is a palindrome!')
    else:
        print('Welp... "' + string + '" is not a palindrome!')
