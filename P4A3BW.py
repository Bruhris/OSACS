# Boris Wang
# Assignment 3 - TI-150 
# Computer Science 20, blk 3
# February 24, 2021

# This program is my own work - BW

def main():
    #makes sure that calculator will run as long as user want to
    running = True
    print("Welcome to Boris' TI-150 Calculator!")
    while running == True:
        #decided what operation the user will do
        operator = input("Please enter operator ( +, -, *, /, remainder, exit ): ")
        #ends program
        if operator.lower() == "exit":
            print("Shutting Calculator Down...")
            running = False
        #adds two numbers
        elif operator == "+":
            numbers = getnum()
            ans = add(float(numbers[0]),float(numbers[1]))
            if ans != None:
                print("Thank you! Your answer is",ans)
        #subtracts two numbers
        elif operator == "-":
            numbers = getnum()
            ans = subtract(float(numbers[0]),float(numbers[1]))
            if ans != None:
                print("Thank you! Your answer is",ans)
        #multiplies two numbers
        elif operator == "*":
            numbers = getnum()
            ans = multiply(float(numbers[0]),float(numbers[1]))
            if ans != None:
                print("Thank you! Your answer is",ans)
        #divides two numbers
        elif operator == "/":
            numbers = getnum()
            ans = divide(float(numbers[0]),float(numbers[1]))
            if ans != None:
                print("Thank you! Your answer is",ans)
        #finds the remainder of two numbers
        elif operator.lower() == "remainder":
            numbers = getnum()
            ans = remainder(float(numbers[0]),float(numbers[1]))
            if ans != None:
                print("Thank you! Your answer is",ans)
        else:
            print("You did not select an operator!")

def getnum():
    #gets the two numbers and stores them in an array
    numbers = []
    num1 = input("Enter the first number: ")
    #while loop used to make sure that the input is a number
    while isinstance(float(num1),float) == False:
        num1 = input("ERROR! Input is not number! Enter first number: ")
    num2 = input("Enter second number: ")
    while isinstance(float(num2),float) == False:
        num2 = input("ERROR! Input is not number! Enter second number: ")
    numbers.extend((num1,num2))
    return numbers

def add(a,b):
    #adds the two numbers and returns them
    print("Calculating",str(a),"+",str(b),"...")
    return a+b

def subtract(a,b):
    #finds which number you want to subtract from which
    first = input("What number do you want to be the minuend? (First or Second): ")
    while first.lower() != "first" and first.lower() != "second":
        first = input("That is not a choice! What number do you want to be the dividend? (1 or 2): ")
    if first.lower() == "first":
        print("Calculating",str(a),"-",str(b),"...")
        return a-b
    else:
        print("Calculating",str(b),"-",str(a),"...")
        return b-a
    
def multiply(a,b):
    #multiplies two numbers
    print("Calculating",str(a),"*",str(b),"...")
    return a*b

def divide(a,b):
    #finds which number you want to divide by which
    first = input("What number do you want to be the dividend? (First or Second): ")
    while first.lower() != "first" and first.lower() != "second":
        first = input("That is not a choice! What number do you want to be the dividend? (1 or 2): ")
    if first.lower() == "first":
        if b == 0:
            print("ERROR! You are dividing by zero! ")
        else:
            print("Calculating",str(a),"/",str(b),"...")
            return a/b
    else:
        print("Calculating",str(b),"/",str(a),"...")
        return b/a

def remainder(a,b):
    #finds which number you want to divide by which to determine remainder
    first = input("What number do you want to dividend? (First or Second): ")
    while first.lower() != "first" and first.lower() != "second":
        first = input("That is not a choice! What number do you want to be the dividend? (1 or 2): ")
    if first.lower() == "first":
        if b == 0:
            print("ERROR! You cannot divide 0! ")
        else:
            print("Calculating",str(a),"%",str(b),"...")
            return a%b
    else:
        print("Calculating",str(b),"%",str(a),"...")
        return b%a
        

if __name__ == "__main__":
    #runs all code under main function
    main()
