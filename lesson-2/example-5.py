# Expressions

# Challenges: Write an expression to solve the problems below

# Area of a rectangle with a width of 12 and a length of 23. Area is length * width
width = 12
length = 23
rectangle_area = width * length
print("rectangle_area: ", rectangle_area)
print(type(rectangle_area))

# Seconds in a day? There 60 secs in a min and 60 mins in an hour and 24 hours in a day
day_in_seconds = 60 * 60 * 24
print("seconds in a day: ", day_in_seconds)
print(type(day_in_seconds))

# Area of a circle with a diameter of 10. Are of a circle is 3.14 * radius * radius 
circle_area = 3.14 * 5**2
print("circle area: ", circle_area)
print(type(circle_area))

# Convert temperature of 72F to C. Formula is: (f - 32) * 5 / 9
temp_f = 72
temp_c = round(((temp_f - 32) * 5 / 9), 2)
print("temp in celcius: ", temp_c)
print(type(temp_c))

# Calculate total cost. Donuts are 0.99 each, specialty donuts are 1.29 each 
# you need 12 regular donuts and 6 specialty donuts
regular_donuts = 12
specialty_donuts = 6
total_cost = round(((regular_donuts * 0.99) + (specialty_donuts * 1.29)), 2)
print("total donut cost: ", total_cost)
print(type(total_cost))