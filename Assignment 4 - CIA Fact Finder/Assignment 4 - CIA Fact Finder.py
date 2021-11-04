# * ***********************************************************************
# Boris Wang
# Exercise 1 - Leap Year
# Computer Science 30 - Block 6
# October 23, 2021

# This program is my own work - BW

import os
import re

r = re.compile(r"[^a-zA-Z0-9-\,]")

def getFile(file_type):
    txt_file = open(file_type, "r+")
    return txt_file

def country_check(file, information):
    with open(information, "r") as chicken:
        lines = chicken.readlines()
    data = []
    for line in file:
        temp = r.sub(" ",line).split()
        data.append(temp)
    print(data)
    while True:
        choice = input("Do you want to check a country? (Y or N) ")
        while choice.lower() != 'y' and choice.lower() != 'n':
            print("That is an invalid input")
            choice = input("Do you want to check a country? (Y or N) ")
        if choice == 'y':
            country = input("Enter the name of the country that you want to check: ").title()
            country_include = False
            for i in data:
                if country in i:
                    print(lines[data.index(i)], end = "")
                    country_include = True
                    break
            if country_include == False:
                print("Sorry the country you were looking for wasn't in the GDP file")
            else:
                break
        while True:
            add_country = input("Do you want to add a countries information to the file? (Y or N)")
            while add_country.lower() != 'y' and add_country.lower() != 'n':
                print("That is an invalid input")
                add_country = input("Do you want to check a country? (Y or N) ")
            if add_country == 'y':
                c_name = input("Enter the name of the country")
                c_values = input("Enter the values that you want to add to data (Only numbers)")
                c_region = input("Enter the region that your country is in")
                add_text = "\n"+c_name+" "+c_values+" "+c_region
                f = open(file, "a")
                f.write(add_text)
            else:
                break
    

def main():
    directory = input("What is the directory where the text files are stored? ")
    if os.path.isdir(directory) == False:
        print("That is not a reachable/valid directory!")
        directory = input("What is the directory where the text files are stored? ")
    os.chdir(directory)
    print("Birth Rate = BR\nGross Domestic Product (In billions) = GDP\nPopulation = P\nUnemployment = U")
    choice = input("What data would you like to get from the list above? ")
    while choice.lower() != 'br' and choice.lower() != 'gdp' and choice.lower() != 'p' and choice.lower() != 'u':
        print("That input in invalid!")
        choice = input("What data would you like to get from the list above? ")
    choice = choice.lower()
    if choice == 'br':
        type = 'birth_rate.txt'
    elif choice == 'gdp':
        type = 'gdp.txt'
    elif choice == 'p':
        type = 'population.txt'
    else:
        type = 'unemployment.txt'
    txt_file = getFile(type)

    country_check(txt_file, type)
    
    
    


if __name__ == '__main__':
    main()
    
