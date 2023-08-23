# Logical errors do not throw errors. They simply just dont 
# return the result we were expecting.

# Solve the problem below. Why is the code below not displaying
# the message that corresponds to the input?

temperature = int(input("What is the temp in Fahrenheit? "))

if temperature < 75:
  print("Whew. It is hot!")
else:
  print("Brrrr. It's cold.")

# looks like the logical operator is backwards. the condition should check if temperature is GREATER THAN (>) instead of less than.