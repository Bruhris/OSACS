# * ***********************************************************************
# Boris Wang
# Assignment 4 - CIA Fact Finder
# Computer Science 30 - Block 6
# October 23, 2021

# This program is my own work - BW

# Import libraries
import os
import time
import re

# Create regular expression pattern to remove certain characters from strings
r = re.compile(r"[^a-zA-Z0-9-,.]")


# Finds the file directory with the correct files
def find_files():
    check = False # Boolean value to check if a proper directory is found
    while check == False:
        # Asks user to input directory
        file_location = input("What is the directory where the text files are stored? ")
        if os.path.isdir(file_location) == False: # If directory is not found
            print("That is not a reachable/valid directory!")
        else:
            os.chdir(file_location) # If directory found, checks if all custom BW txt files are found
            if os.path.exists('./birth_rateBW.txt') == False or os.path.exists('./gdpBW.txt') == False or os.path.exists('./populationBW.txt') == False or os.path.exists('./unemploymentBW.txt') == False:
                print("You are missing the BW text files from the directory!")
            else: # If all conditions satisfied, returns true
                check = True
    os.chdir(file_location) # Changes the file directory to where the user specified

# Gets the statistics of the country using the text file
def get_country_stats(file, name):
    with open(file, "r+") as txt_file: # Gets the line where country, values and regions are and puts them into a list between each space
        for line in txt_file:
            if name in line:
                country_info = r.sub(" ",line).split()
                break
    for element in country_info: # Gets the value from the country and the region where the country is
        if element[0].isdigit() == True:
            country_value = element
            country_region = " ".join(country_info[country_info.index(element)+1:])
    # Checks which file was being checked and prints a custom message based on the file
    if file == "gdpBW.txt":
        print("The Gross Domestic Product of",name,"is $"+str(country_value))
    elif file == "birth_rateBW.txt":
        print("The birth rate of",name,"is "+str(country_value)+" births/1000 population")
    elif file == "populationBW.txt":
        print("The population of",name,"is "+str(country_value))
    elif file == "unemploymentBW.txt":
        print("The unemployment rate of",name,"is "+str(country_value)+"%")
    print(name,"is also located in the region of:",country_region)

# Compares the statistics of two countries
def compare_countries(first, second, file):
    with open(file, "r+") as txt_file: # Gets the lines where the countries that the user specified are
        for line in txt_file:
            if first in line:
                first_info = r.sub(" ",line).split()
            if second in line:
                second_info = r.sub(" ",line).split()
    for element in first_info: # Gets the values and regions of the two countries
        if element[0].isdigit() == True:
            first_value = "".join(u for u in element if u not in (","))
            first_region = " ".join(first_info[first_info.index(element)+1:])
    for element in second_info:
        if element[0].isdigit() == True:
            second_value = "".join(u for u in element if u not in (","))
            second_region = " ".join(second_info[second_info.index(element)+1:])
    # Outputs difference of two values and a custom message based on the file selected
    if file == "gdpBW.txt":
        print("The difference in Gross Domestic Product between",first,"and",second,"is $"+str(abs(int(first_value)-int(second_value))))
    elif file == "birth_rateBW.txt":
        print("The difference in birth rate between",first,"and",second,"is "+str(round(abs(float(first_value)-float(second_value)),2))+" births/1000 population")
    elif file == "populationBW.txt":
        print("The difference in population between",first,"and",second,"is "+str(abs(int(first_value)-int(second_value))))
    elif file == "unemploymentBW.txt":
        print("The difference in unemployment between",first,"and",second,"is "+str(round(abs(float(first_value)-float(second_value)),2))+"%")
    print(first,"is located in the region of:",first_region+", whereas",second,"is located in:",second_region)
    
# Gets user to input their own data to add to the text files
def add_data(file):
    # Name of country
    c_name = input("What is the name of your country? ")
    while True: # Error check to make sure that only numbers are inputed for the data values of country
        try:
            c_values = input("Enter the values that you want to add to data (Only numbers): ")
            float(c_values)
            break
        except ValueError:
            print("That is an invalid input!")
    # Enter region of country
    c_region = input("Enter the region that your country is in: ")
    # Places data into a string and writes it in file, giving the user a message saying that the text has been successfully written in the file
    add_text = "\n"+c_name+"    "+str(c_values)+"   "+c_region
    with open(file, "a") as txt_file:
        txt_file.write(add_text)
    print("Your data has been successfully added to the text file: "+file)


def main():
    find_files()
    # Assigns a list called countries to the 25 most powerful countries in the world and displays them
    countries = ["United States", "China", "Russia", "Germany", "United Kingdom", "Japan", "France", "South Korea", "Saudi Arabia", "United Arab Emirates",
    "Israel", "Canada", "India", "Turkey", "Italy", "Australia", "Costa Rica", "Switzerland", "Spain", "Brazil", "Sri Lanka", "Singapore", "Iraq", "Qatar", "Netherlands"]
    print("Here is a list of the 25 strongest countries in the world (According to: https://worldpopulationreview.com/country-rankings/most-powerful-countries):")
    for i in countries:
        time.sleep(0.4)
        print(str(countries.index(i)+1)+". "+i)
    while True:
        # User picks between 4 options
        choice = input("Would you like to view one of the countries stats (V), compare two of the strongest countries (C), add your own country to one of the text files (A) or exit the program (E)? ").lower()
        while choice != 'v' and choice != 'c' and choice != 'a' and choice != 'e': # Error checking
            print("That is an invalid input")
            choice = input("Would you like to view a countries stats (V), compare two of the strongest countries (C), add your own country to a text file (A) or exit the program (E)? ").lower()
        if choice == 'v': # View stats of country
            user_country = input("Which country's statistics would you like to view? ").title() # Input a valid country
            while user_country not in countries:
                print("That is an invalid country!")
                user_country = input("Which country's statistics would you like to view? ").title()
            print("List of data files:\nBirth Rate = BR\nGross Domestic Product = GDP\nPopulation = P\nUnemployment = U")
            data_selection = input("Which of the following statistics of {0} would you like to view? ".format(user_country)).lower() # Pick which data of the selected country the user wants to view
            while data_selection != 'br' and data_selection != 'gdp' and data_selection != 'p' and data_selection != 'u':
                print("That is an invalid input")
                data_selection = input("Which of the following statistics of {0} would you like to view? ".format(user_country)).lower()
            if data_selection == 'br': # Runs the get_country_stats() method using custom arguments
                get_country_stats("birth_rateBW.txt", user_country)
            elif data_selection == 'gdp':
                get_country_stats("gdpBW.txt", user_country)
            elif data_selection == 'p':
                get_country_stats("populationBW.txt", user_country)
            elif data_selection == 'u':
                get_country_stats("unemploymentBW.txt", user_country)
        elif choice == 'c': # Compare two countries
            first_country = input("What is the first country you want to compare with? ").title() # Gets the first country
            while first_country not in countries:
                print("That is an invalid country!")
                first_country = input("What is the first country you want to compare with? ").title()
            second_country = input("What is the second country you want to compare with? ").title() # Gets the second country
            while second_country not in countries:
                print("That is an invalid country!")
                second_country = input("What is the second country you want to compare with? ").title()
            print("List of data files:\nBirth Rate = BR\nGross Domestic Product (In billions) = GDP\nPopulation = P\nUnemployment = U") # Selects which data from the selected countries the user wants to compare
            data_selection = input("Which of the following statistics would you like to compare? ").lower()
            while data_selection != 'br' and data_selection != 'gdp' and data_selection != 'p' and data_selection != 'u':
                print("That is an invalid input")
                data_selection = input("Which of the following statistics would you like to compare? ").lower()
            if data_selection == 'br': # Run compare_countries() method with custom arguments
                compare_countries(first_country,second_country, "birth_rateBW.txt")
            elif data_selection == 'gdp':
                compare_countries(first_country,second_country, "gdpBW.txt")
            elif data_selection == 'p':
                compare_countries(first_country,second_country, "populationBW.txt")
            elif data_selection == 'u':
                compare_countries(first_country,second_country, "unemploymentBW.txt")
        elif choice == 'a':
            print("List of data files:\nBirth Rate = BR\nGross Domestic Product (In billions) = GDP\nPopulation = P\nUnemployment = U")
            add_file = input("What file do you want to add your country to? ").lower() # Select which file to add data to
            while add_file != 'br' and add_file != 'gdp' and add_file != 'p' and add_file != 'u':
                print("That is an invalid input")
                add_file = input("What file do you want to add your country to? ").lower()
            if add_file == 'br':
                add_data("birth_rateBW.txt")
            elif add_file == 'gdp':
                add_data("gdpBW.txt")
            elif add_file == 'p':
                add_data("populationBW.txt")
            elif add_file == 'u':
                add_data("unemploymentBW.txt")
        else:
            print("Thanks for using my program!") # User exits the program
            break
    

if __name__ == '__main__':
    main()
    
