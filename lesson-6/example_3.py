'''
Deep down inside you're a cat person! 🐈
Cat people collect cats and obsess over 
cat details! 
'''

cat_names = []

# TODO: Print the cat list! 
print(cat_names)

# TODO: Print the cat_names after each step 
# below, you're obsessed remember! 


# TODO: You just got your first cat: "Bert"
# Add it to the cat_names list with append!
cat_names.append("Bert")
print(cat_names)

# You just got two more cats! Someone 
# put them in an array and left them at your
# house: ["Clawdia", "Eunice"]
# TODO: Extend at_names with the new cats in the 
# list above. Use cat_names.extend()
house = ["Clawdia", "Eunice"]
cat_names.extend(house)
print(cat_names)

# TODO: You found a cat walking home yesterday
# It's name is "Alfie". You always keep your 
# cats organized in alphabetical, you're
# obsessed remember? Use cat_names.prepend()
cat_names.insert(0, "Alfie")
print(cat_names)

# TODO: You just found another cat named "Duff"
# Put Duff in the cat_names in alphabetical order 
# use cat_names.insert()
cat_names.insert(3, "Duff")
print(cat_names)

# TODO: These Cats are ruining your furniture
# Give one away. Use cat_names.remove() to 
# remove "Eunice"
cat_names.remove("Eunice")
print(cat_names)

# TODO: I think "Alfie" has to go he keeps 
# horking up fur balls! he should be first in 
# the list you can use: cat_names.pop()
cat_names.pop(0)
print(cat_names)

# TODO: Actually you've had a revelation and 
# decided you're a dog person after all. Clear
# the cat_names with cat_names.clear()
cat_names.clear()
print(cat_names)