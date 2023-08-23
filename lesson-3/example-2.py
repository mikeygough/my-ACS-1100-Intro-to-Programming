#TODO: write a function called subtract_twenty that takes in an integer 
# parameter and returns the integer minus 20
def subtract_twenty(base_number):
    result = base_number - 20
    return result

#TODO: call subtract_twenty() with the value 40 and display the result
print(subtract_twenty(40))

#TODO: call subtract_twenty() with the value -100 and display the result
print(subtract_twenty(-100))

#TODO: write a function called add_hello that takes in a string parameter 
# representing a name and returns a new string with the name and " hello!"
def add_hello(base_string):
    result = base_string + " hello!"
    return result

#TODO: call add_hello with the value of your name and display the result
print(add_hello("Mikey"))

#for example if I gave "Jess" to add_hello()
#Jess hello! would be displayed

#TODO: Take a look at your custom calculator. Ask yourself where you
#can add a function? 
#
# You should be able to add a function that performs
# the custom calculation.
# 
# It's also possible that your code could be broken into more than one function
# Think carefully about each of the functions you might create. They should each 
# be responsible for one task or operation. 
# 
# Make these changes. 

import datetime

print("\nWecome to the Days-Between Calculator!")
print("The Days-Between Calculator calculates the absolute number of days between a start_date and end_date.")
print("Dates should be entered in the format YYYY-MM-DD. For example, August 1, 2023 entered as 2023-08-01.\n")

def get_date(user_date):
    """''get_date() prompts a user for a date and returns a datetime object of that date 
        user_date should be a string to format the input prompts. for example, 'start_date'"""
    
    d = input(f"What is the {user_date}? (In the format YYYY-MM-DD): ")

    # error checking
    while len(str(d)) != 10:
        print("Invalid Format! Please try again.")
        d = input(f"What is the {user_date}? (In the format YYYY-MM-DD): ")

    # select year, month and day. convert to int
    year = int(d[0:4])
    month = int(d[5:7])
    day = int(d[8:10])

    # create datetime object
    d = datetime.datetime(year, month, day)

    return d

start_date = get_date("start_date")
end_date = get_date("end date")

# calculate days_between
days_between = abs((start_date - end_date).days)

# print result
print(f"Days Between: {days_between:,}\n")