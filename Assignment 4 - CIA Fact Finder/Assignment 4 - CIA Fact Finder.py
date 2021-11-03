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

def main():
    gdp = []
    birth_rate = []
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
    for line in txt_file:
        temp = r.sub(" ",line).split()
        gdp.append(temp)
    country = input("What country do you want to check? ")
    country_include = False
    for i in gdp:
        if country in i:
            print(i[0],i[1],i[2])
            country_include = True
            break
    if country_include == False:
        print("Sorry the country you were looking for wasn't in the GDP file")
        add_data = input("Do you want to add a country with their GDP and region to the file? (Y or N)")
        

    txt_file.close()
    
    
    


if __name__ == '__main__':
    main()
    
