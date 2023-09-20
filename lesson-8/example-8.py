'''
Before Sunday Night Football, you want to go shopping for your favorite snacks! 

Let's create a shopping list with your favorite snacks to eat!
'''

#TODO: create a list of strings containing your favorite snacks
favorite_snacks = ['Cheeseburgers', 'Ribs', 'Kale Salad', 'Soy Milk']
favorite_snacks = "\n".join(favorite_snacks)


#TODO: open a new file called "shopping_list.txt" for write
output_file_name = 'shopping_list.txt'

# #TODO: finish this loop to write your favorite snacks to the shopping_list.txt file
output_file = open(output_file_name, "w")

for snack in favorite_snacks:
    output_file.write(snack)

output_file.close()

# Notice how the above code overwrites the data with each loop. 
# Let's modify our code to write multiple lines of code to the file!

'''
TODO: 

1. Creating a function called write_shopping_list() that has one parameter called snacks. This function takes a list of strings.

2. You function should write to the file using .writelines() 

'''
def write_shopping_list(snacks):
    output_file = open(output_file_name, "w")
    output_file.writelines(favorite_snacks)
    output_file.close()
