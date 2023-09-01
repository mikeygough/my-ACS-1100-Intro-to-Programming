'''
TODO: Now it's your turn!

Write a function that takes in the temperature in degrees F.

If the temperature is greater than 50, return "It's hot!"

else return "Brr!"

Call your function twice with some different temperature values and print the results.
'''


def weather_condition(temp):
  if temp > 50:
    return "It's hot!"
  else:
    return "Brr!"

print(weather_condition(45)) #Brr!
print(weather_condition(85)) #It's hot!