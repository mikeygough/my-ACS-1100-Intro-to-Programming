# Homework: Your job is to make a custom calculator. 
# Your calculator should accept at least three values. 

# For example height, width, length

# It should print a prompt that makes it clear what 
# is being calculated. 

# For example: 
# Enter height, width, and length to calculate the area of a cube
# Height: 3
# Width: 4
# Length: 2

# After accepting input the calculator should perform 
# an accurate calculation and display the results in 
# a clear and well formatted message. 

# For example: A cube with a height of 3, width of 4, and length of 2 has an area of 24

# You can accept string input that becomes part of the descirption. 
# For example: Input units: inches

# Be sure to convert your numeric values to numbers before performing math operations!

''' !! non-function version !! '''

import datetime

print("\nWecome to the Days-Between Calculator!")
print("The Days-Between Calculator calculates the absolute number of days between a start_date and end_date.")
print("Dates should be entered in the format YYYY-MM-DD. For example, August 1, 2023 entered as 2023-08-01.\n")

# -- get user input start_date
start_date = input("What is the start_date? (In the format YYYY-MM-DD): ")

# error checking
while len(str(start_date)) != 10:
    print("Invalid Format! Please try again.")
    start_date = input("What is the start_date? (In the format YYYY-MM-DD): ")

# select year, month and day. convert to int
year = int(start_date[0:4])
month = int(start_date[5:7])
day = int(start_date[8:10])

# create datetime object
start_date = datetime.datetime(year, month, day)

# -- get user input end_date
end_date = input("What is the end_date? (In the format YYYY-MM-DD): ")

# error checking
while len(str(end_date)) != 10:
    print("Invalid Format! Please try again.")
    end_date = input("What is the end_date? (In the format YYYY-MM-DD): ")

# select year, month and day. convert to int
year = int(end_date[0:4])
month = int(end_date[5:7])
day = int(end_date[8:10])

# create datetime object
end_date = datetime.datetime(year, month, day)

# calculate days_between
days_between = abs((start_date - end_date).days)

# print result
print(f"Days Between: {days_between:,}\n")


''' !! function version !! '''
import datetime

print("\nWecome to the Days-Between Calculator!")
print("The Days-Between Calculator calculates the absolute number of days between a start_date and end_date.")
print("Dates should be entered in the format YYYY-MM-DD. For example, August 1, 2023 entered as 2023-08-01.\n")

def get_date(user_date):
    """''get_date() prompts a user for a date and returns a datetime object of that date (YYYY-MM-DD)
        user_date: a string to format the input prompts. for example, user_date='start_date'"""
    
    # prompt user
    d = input(f"What is the {user_date}? (In the format YYYY-MM-DD): ")

    # error checking, ensure length matches YYYY-MM-DD
    while len(str(d)) != 10:
        print("Invalid Format! Please try again.")
        d = input(f"What is the {user_date}? (In the format YYYY-MM-DD): ")

    # select year, month and day. convert to int
    year = int(d[0:4])
    month = int(d[5:7])
    day = int(d[8:10])

    # create datetime object
    d = datetime.datetime(year, month, day)

    # return d as a datetime object
    return d

start_date = get_date("start_date")
end_date = get_date("end date")

# calculate days_between
days_between = abs((start_date - end_date).days)

# print result
print(f"Days Between: {days_between:,}\n")