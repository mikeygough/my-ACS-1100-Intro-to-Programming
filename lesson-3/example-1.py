def greet_by_name(name):
	greeting = "Hello, " + name + "!"
	return greeting

a = greet_by_name("Amy")
b = greet_by_name("Bob")
c = greet_by_name("Cat")
d = greet_by_name("Dan")

# Print the variables above to the console
print(a)
print(b)
print(c)
print(d)

# What type is returned? How can you check the type? Do it that here:
# i'd guess string, we can check with print(type(a))
def add_ten(number): 
	new_number = number + 10
	return new_number

add_ten(60)
add_ten(30)

# How can you save the values returned by the add_ten function?
# store them in a variable...
first_sum = add_ten(60)
second_sum = add_ten(30)

# Print the values returned by the two calls to add_ten above:
print(first_sum)
print(second_sum)

# Use add_ten to add 10 to the total of the first two calls to add_ten. 
ans = add_ten(first_sum + second_sum)
print(ans)
# The answer should be 120. Print the result below. 

asci_art_scuba = '''         o
        o  o
        o o o
      o
     o    ______          ______
     _ *o(_||___)________/___
   O(_)(       o  ______/    \\
  > ^  `/------o-'            \\
D|_|___/'''

print(asci_art_scuba)

asci_art_mushroom = """       .
        ('
        '|
        |'
       [::]
       [::]   _......_
       [::].-'      _.-`.
       [:.'    .-. '-._.-`.
       [/ /\   |  \        `-..
       / / |   `-.'      .-.   `-.
      /  `-'            (   `.    `.
     |           /\      `-._/      \\
     '    .'\   /  `.           _.-'|
    /    /  /   \_.-'        _.':;:/
  .'     \_/             _.-':;_.-'
 /   .-.             _.-' \;.-'
/   (   \       _..-'     |
\    `._/  _..-'    .--.  |
 `-.....-'/  _ _  .'    '.|
          | |_|_| |      | \  (o)
     (o)  | |_|_| |      | | (\'/)
    (\'/)/  ''''' |     o|  \;:;
     :;  |        |      |  |/)
 LGB  ;: `-.._    /__..--'\.' ;:
          :;  `--' :;   :;"""

print(asci_art_mushroom)