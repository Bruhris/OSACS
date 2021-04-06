# Boris Wang
# Assignment 1 - Cryptography
# Computer Science 20, blk 3
# April 5, 2021

# This program is my own work - BW


def goAgain():
    # Asks if the user wants to use the program again
    print("Do you want to go again? (Y or N)")
    choice = input()
    # If user does not input the expected input, will continually ask them
    while choice.lower() != 'y' and choice.lower() != 'n':
        print("That is an invalid response!")
        choice = input()
    # If no, will end the program
    if choice.lower() == 'n':
        print("See you next time!")
        return True
    # If yes, will continue the program
    else:
        return False


def decrypt(text, shift):
    # Create an empty string that we will return as the result of function
    ans = ""
    # Goes through the entire text
    for i in range(len(text)):
        char = text[i]
        # Checks if character is uppercase, lowercase or a digit and calculates the ASCII value of the original character
        # Then adds character to empty string
        if (char.isupper()):
            ans += chr((ord(char)-shift - 65) % 26 + 65)
        elif(char.islower()):
            ans += chr((ord(char)-shift - 97) % 26 + 97)
        elif(char.isdigit()):
            ans += (int(char)-shift) % 10
        else:
            ans += char
    # Will return the whole string decrypted
    return ans


def encrypt(text, shift):
    # Create an empty string that we will return as the result of function
    ans = ""
    # Goes through the entire text
    for i in range(len(text)):
        char = text[i]
        # Checks if character is uppercase, lowercase or a digit and calculates the ASCII value of the encrypted character
        # Then adds character to empty string
        if (char.isupper()):
            ans += chr((ord(char) + shift - 65) % 26 + 65)
        elif(char.islower()):
            ans += chr((ord(char) + shift - 97) % 26 + 97)
        elif(char.isdigit()):
            ans += (int(char) + shift) % 10
        else:
            ans += char
    # Will return the whole string encrypted
    return ans


# Starts and runs the program
if __name__ == "__main__":
    quit = False
    # Creates a while loop that asks for user input
    while quit == False:
        print("Do you want to encode or decode some text? (E or D): ")
        choice = input().lower()
        # Checks if input is valid and if not, continually asks the user for correct input
        while choice != 'e' and choice != 'd':
            print("That is no a valid input!")
            print("Do you want to encode or decode some text? (E or D): ")
            choice = input()
        # If user wants to encode some text, will ask for the text they want to encode and the shift
        if choice == 'e':
            print("Input the text you want to encode: ")
            plain = input()
            print("Input the amount you want to shift by: ")
            shift = int(input())
            # Will run encrypt function that takes the two inputs as arguments
            result = encrypt(plain, shift)
            # Prints out the original inputed text and the encode text
            print("Original Text: "+plain)
            print("Encoded Text: "+result)
            # Checks if user wants to use the program again
            quit = goAgain()
        else:
            # If user wants to decode some text, will ask fro the text they want to decode and the shift
            print("Input the text you want to decode: ")
            coded = input()
            print("Input the amount you want to shift by: ")
            shift = int(input())
            # Will run decrypt functions that takes the two inputs as arguments
            result = decrypt(coded, shift)
            # Prints out the original text and encoded text
            print("The Encoded Text: "+coded)
            print("The Original Text: "+result)
            # Checks if user wants to use program again
            quit = goAgain()
