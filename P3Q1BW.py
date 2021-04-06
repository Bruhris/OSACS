# Boris Wang
# Assignment 2 - For Loops
# Computer Science 20, blk 3
# February 17, 2021

# This program is my own work - BW

response1 = input("Enter a number 1 or greater: ")

while int(response1)<=0 :
    response1 = input("     Too small - Try again: ")

print("")
print("Counting from 0 to", str(response1)+":")

for i in range(0,int(response1)+1):
    print(i, end = '    ')
print("\n")
operation = input("Choose math operation (+, -, *): ")

while str(operation) != "+" and str(operation) != "-" and str(operation) != "*":
    operation = input("   Invalid input - Try again: ")

print("")
print("Table for", str(response1),"using",operation+":")

if operation == "+":
    for k in range(1,11):
        print(int(response1),"+",k,"=",int(response1)+k)
elif operation == "-":
    for j in range(1,11):
        print(int(response1),"-",j,"=",int(response1)-j)
elif operation == "*":
    for x in range(1,11):
        print(int(response1),"*",x,"=",int(response1)*x)

#Extension
#if int(response1)%2==1:
#    print("As an extension, I know that your number is odd : )")
#else:
#    print("As an extension, I know that your number is even : )")