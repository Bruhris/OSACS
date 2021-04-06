# Boris Wang
# Exercise 2 - Python String
# Computer Science 20, blk 3
# March 3, 2021

# This program is my own work - BW

def sum_digits(ogstring):
    #runs through the string and everytime it finds an integer, adds it to the total
    total = 0
    for i in ogstring:
        if(i.isdigit() == True):
            total += int(i)
    print("Digit Sum: ",total)

def explore_chars(ogstring):
    #prints out the information needed about the user inputed string as shown below
    print("Original:  ",ogstring)
    print("Length:    ",len(ogstring),"chars")
    print("2nd char:  ",ogstring[1])
    print("2nd last:  ",ogstring[-2])
    print("Switched:  ",ogstring[-3:]+ogstring[3:-3]+ogstring[0:3])

def get_input():
    #makes sure that the input is valid and if not, will continue to ask the user for input
    line = input("Enter 10 or more chars ending with a period:\n-> ")
    while len(line) < 10 or line[-1] != ".":
        print("That is an invalid input!")
        line = input("Enter 10 or more chars ending with a period:\n-> ")
    return line

def explore_string():
    #runs all the functions under one function
    string = get_input()
    explore_chars(string)
    sum_digits(string)

def main():
    #runs the function which, intern runs all the other functions
    explore_string()

if __name__ == "__main__":
    #runs main function
    main()