# * ***********************************************************************
# Boris Wang
# Assignment 4 - CIA Fact Finder
# Computer Science 30 - Block 6
# October 23, 2021

# This program is my own work - BW

import os
import statistics
import re

r = re.compile(r"[^a-zA-Z0-9-,.]")

def getFile(file_type):
    txt_file = open(file_type, "r+")
    return txt_file

def compare_country(file, data):
    while True:
        while True:
            first_country = input("What is the first country you want to compare? ")
            located_first = False
            for i in data:
                if first_country in i:
                    first_data = i
                    located_first = True
                    break
            if located_first == False:
                print("Sorry that country is not in the list. Please select a valid country!")
            else:
                break
        while True:
            second_country = input("What is the second country you want to compare? ")
            located_second = False
            for i in data:
                if second_country in i:
                    second_data = i
                    located_second = True
                    break
            if located_second == False:
                print("Sorry that country is not in the list. Please select a valid country!")
            else:
                break
        print(first_data)
        print(second_data)
        for element in first_data:
            if element[0].isdigit() == True:
                first_value = element
                first_value = "".join(u for u in first_value if u not in (","))
        for element in second_data:
            if element[0].isdigit() == True:
                second_value = element
                second_value = "".join(u for u in second_value if u not in (","))
        print("The difference between the values of "+first_country+" and "+second_country+" is:",round(abs(float(first_value) - float(second_value)),2))
        choice = input("Do you want to compare another two countries or pick a different option (A or E) ").lower()
        while choice != 'a' and choice != 'e':
            print("That is an invalid input!")
            choice = input("Do you want to compare another two countries or pick a differernt option? (A or E) ").lower()
        if choice == 'e':
            break

            
        

def country_check(file, data):
    while True:
        country = input("Enter the name of the country that you want to check or 'E' to pick a different option: ").title()
        if country != 'E':
            country_include = False
            for i in data:
                if country in i:
                    print("Name of Country   Value    Region")
                    for j in data[data.index(i)]:
                        print(j,end=" ")
                    print()
                    country_include = True
                    break
            if country_include == False:
                print("Sorry the country you were looking for wasn't in the GDP file")
        else:
            break


def add_country(file, data):
    while True:
        c_name = input("Enter the name of the country: ")
        while True:
            try:
                c_values = input("Enter the values that you want to add to data (Only numbers): ")
                float(c_values)
                break
            except ValueError:
                print("That is an invalid input!")
        c_region = input("Enter the region that your country is in: ")
        add_text = "\n"+c_name+" "+str(c_values)+" "+c_region
        file.write(add_text)
        temp_list = [c_name,c_values,c_region]
        data.append(temp_list)
        add_country = input("Do you want to add another countries information to the file or pick a different option? (A or E) ").lower()
        while add_country != 'a' and add_country != 'e':
            print("That is an invalid input")
            add_country = input("Do you want to add a countries information to the file or pick a different option? (A or E) ").lower()
        if add_country == 'e':
            return data
            break

def find_files():
    file_location = input("What is the directory where the text files are stored? ")
    while os.path.isdir(file_location) == False:
        print("That is not a reachable/valid directory!")
        file_location = input("What is the directory where the text files are stored? ")
    os.chdir(file_location)
    while os.path.exists('./birth_rate.txt') == False or os.path.exists('./gdp.txt') == False or os.path.exists('./population.txt') == False or os.path.exists('./unemployment.txt') == False:
        print("You are missing some files from the directory!")
        file_location = input("What is the directory where the text files are stored? ")
    return file_location


def main():
    file_location = find_files()
    os.chdir(file_location)
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
    file_data = []
    for line in txt_file:
        temp = r.sub(" ",line).split()
        file_data.append(temp)
    print(file_data)
    while True:
        options = input("Do you want to view the stats of a country, add a countries data to the text files, compare two countries or exit the program?\nStats = 'S'\nCompare = 'C'\nAdd = 'A'\nExit = 'E'\n").lower()
        while options != 's' and options != 'c' and options != 'a' and options != 'e':
            print("That input is invalid")
            options = input("Do you want to view the stats of a country, add a countries data to the text files, compare two countries or exit the program? ")
        if options == 's':
            country_check(txt_file, file_data)
        elif options == 'a':
            file_data = add_country(txt_file, file_data)
        elif options == 'c':
            compare_country(txt_file, file_data)
        else:
            print("Thats for using the program!")
            break
        
    
    


if __name__ == '__main__':
    main()
    
