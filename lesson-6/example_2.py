''''
Welcome to Jess + Joi's Dog Kennel 🦴

Every dog is stored at an index

For example: 
index 0 Henry. 🐕‍🦺
index 2 Wuffles. 🐕
'''

# List of dog names
dogs = ["Henry", "Rookie", "Wuffles", "Nugget"]

# Print the first dog's name 
print(dogs[0])

# TODO: Print the second dog
print(dogs[1])

# TODO: Print the third dog
print(dogs[2])

# TODO: Print the fouth dog
print(dogs[3])

# TODO: Use negative indexing to print the last dog
print(dogs[-1])

# TODO: Use negative indexing to print the names of the other dogs
print(dogs[-2:])

# Joi and Jess want to split up the work at the kennel. Using list 
# slicing, assign Joi two dogs

# listname[start:stop]

joi_dogs = dogs[0:3]
print(joi_dogs)

# TODO: Assign jess the remaining dogs and print Jess' dogs
jess_dogs = dogs[3:]

# TODO: A new dog is visiting the kennel. Make up a name and 
# append that dog to the list use: dogs.append("Name")
new_dog = "Buddy"
dogs.append(new_dog)

# TODO: Print the dogs list to check the dogs. 
print(dogs)

# num_visit stores the number of times a dog has visited the kennel
num_visit = [2, 3, 5, 2]

# TODO: The new dog just visited for the first appead a 1 to the 
# num_visits list:
num_visit.append(1)

# TODO: Print each dog and the number of times it has visited: 
print(f"{dogs[0]} has visited {num_visit[0]}")

# TODO: Put the code above into a function that will print the
# dogs and visits
def dogs_visits(dog_id, dogs=dogs, num_visits=num_visit):
    print(f"{dogs[dog_id]} has visited {num_visit[dog_id]}")

# TODO: Imagine it's a new week and the dog's have all visited one 
# more time. Increase each dog's visit by 1
num_visit[0] += 1 # add one to Henry's visits

["Henry", "Rookie", "Wuffles", "Nugget"]
# add 1 to Rookie
num_visit[1] += 1
# add 1 to Wuffles
num_visit[2] += 1
# add 1 to Nugget
num_visit[3] += 1

# TODO: Print the names and visits of all dogs again! 
for i in range(len(dogs)):
    dogs_visits(i)


# TODO: Count the dogs in the list with code! Use len()
# to print the number of dogs in the list: len(dogs)
print(len(dogs))

# TODO: Write a function that takes the index of a dog
# and prints name of the dog and the number of visits. 
def dogs_data(dog_id, dogs=dogs, num_visit=num_visit):
    print(f"Dog Name: {dogs[dog_id]} \nVisit: {num_visit[dog_id]}")

# TODO: Modify your function above, the one that prints 
# all of the dogs, to use this function!
for i in range(len(dogs)):
    dogs_data(i)

# TODO: The kennel is doing well. We need to know how much 
# money we are making sittting dogs. Look up the amount 
# a kennel might charge for sitting a dog per day. I found
# $21 to $40. Define a variable cost_per_day. 
cost_per_day = 60

# TODO: Write a function that returns the amount made for 
# sitting a dog. This function should take the index of the
# dog as a parameter and return the num_visit for that dog 
# times the cost_per_day. 
def dog_revenue(dog_id, num_visits=num_visit, cost_per_day=60):
    return num_visit[dog_id] * cost_per_day

# TODO: Using the function you created in the previous 
# step print a billing message for each dog. Include the 
# dog's name, the number of visits, cost per visit, and 
# the total bill: 
for i in range(len(dogs)):
    print(f"""Dog Name: {dogs[i]}\n
              Number of Visits: {num_visit[i]}\n
              Cost per Visit: {cost_per_day}\n
              Total Bill: {dog_revenue(i)}""")

# TODO: Print a billing message for each dog in your list: 
for i in range(len(dogs)):
    print(f"""Dog Name: {dogs[i]}\n
              Number of Visits: {num_visit[i]}\n
              Cost per Visit: {cost_per_day}\n
              Total Bill: {dog_revenue(i)}""")
