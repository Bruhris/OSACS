# Day of the Year guessing game

month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"] # Assigns the months of the year
num_days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # Assigned the number of days corresponding to each month


def calendar(month_names, num_days_in_month):
   if len(month_names) != len(num_days_in_month):
       return []

   dates = []
   idx = 0

   while idx < len(month_names):
       for date in range(1, num_days_in_month[idx] + 1):
           dates.append(month_names[idx] + " " + str(date))
       idx = idx + 1
   return dates


first = calendar(month_names, num_days_in_month)


def guess_game(first = calendar(month_names, num_days_in_month)):
   mid = len(first)//2

   val = is_earlier(first[mid])

   if val == 1:
       return guess_game(first[:mid + 1])
   elif val == 2:
       return guess_game(first[mid - 1:])
   else:
       return first[mid]


def is_earlier(guess = 10):
   return int(input("{}: 1 - earlier, 2 - later, 3 - equal?: ".format(guess))) # Asks the user for 


if __name__ == '__main__':
   print ('Think of a specific date in any year')
   print ('e.g., Jan 1 or Feb 29 or Jul 4 or Dec 25')
   print ('Truthfully answer "Yes" or "No" to the following questions')
   print ('I will determine the date in ten questions or less') # Explains the game to user

   print(guess_game()) 

