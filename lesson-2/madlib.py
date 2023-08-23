# Homework: Create a madlib. Imagine a story where some of the words are 
# supplied by user input. Using python you will use input to collect 
# words for a story and then display the story. 
# Use input to collect each word to a variable
# Use an f string to display the story
# Your madlib must collect at least 6 words!

print("Welcome to MadLibs Vacations! Provided by MadLibs 1988")
print("Copyright © 1988 by Price Stern Sloan, a division of Penguin Putnam Books for Young Readers, New York.\n")

print("You will soon be prompted for several words.")
print("Once all the words are collected we'll reveal your Madlib.")

# collect input
a1 = input("ADJECTIVE: ")
a2 = input("ADJECTIVE: ")
n1 = input("NOUN: ")
n2 = input("NOUN: ")
pn1 = input("PLURAL NOUN: ")
game = input("GAME: ")
pn2 = input("PLURAL NOUN: ")
ving1 = input("VERB ENDING IN 'ING': ")
ving2 = input("VERB ENDING IN 'ING': ")
pn3 = input("PLURAL NOUN: ")
ving3 = input("VERB ENDING IN 'ING': ")
n3 = input("NOUN: ")
plant = input("PLANT: ")
part_of_body = input("PART OF BODY: ")
place = input("PLACE: ")
ving4 = input("VERB ENDING IN 'ING': ")
a3 = input("ADJECTIVE: ")
number = input("NUMBER: ")
pn4 = input("PLURAL NOUN: ")

# format string
madlib = f'''A vacation is when you take a trip to some {a1} place
with your {a2} family. Usually you go to some place
that is near a/an {n1} or up on a/an {n2}.
A good vacation place is one where you can ride {pn1}
or play {game} or go hunting for {pn2}. I like
to spend my time {ving1} or {ving2}.
When parents go on a vacation, they spend their time eating
three {pn3} a day, and fathers play golf, and mothers
sit around {ving3}. Last summer, my little brother
fell in a/an {n3} and got poison {plant} all
over his {part_of_body}. My family is going to go to (the)
{place}, and I will practice {ving4}. Parents
need vacations more than kids because parents are always very
{a3} and because they have to work {number}
hours every day all year making enough {pn4} to pay
for the vacation.'''

# print
print("Your vacation MadLib...\n")
print(f"{madlib}\n")
print("Thanks for playing!")
print("MadLibs Source: https://www.madlibs.com/wp-content/uploads/2016/04/VacationFun_ML_2009_pg15.pdf")