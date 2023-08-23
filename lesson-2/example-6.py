
# Convert the lyrics into string:

# When I find myself in times of trouble, Mother Mary comes to me
# Speaking words of wisdom, let it be
# And in my hour of darkness she is standing right in front of me
# Speaking words of wisdom, let it be
# Let it be, let it be, let it be, let it be
# Whisper words of wisdom, let it be

# Each line should be assigned to its own variable! 
# Look for patterns and use different string operators

# Example:
# + - concatenation (adding two strings together)
# * - generate multiple copies of the string

be = "let it be"
wisdom = "words of wisdom"

line_1 = "When I find myself in times of trouble, Mother Mary comes to me"

line_2 = "Speaking " + wisdom + ', ' + be

line_3 = "And in my hour of darkness she is standing right in front of me"

line_4 = line_2

line_5 = be * 4


# Whisper words of wisdom, let it be

line_6 = "Whisper " + wisdom + ", " + be

# Challenge! Put the song together and print 
# the lyrics to the console:

print(f"""
{line_1}
{line_2}
{line_3}
{line_4}
{line_5}
""")

# DRY is an accronym for Don't Repeat Yourself! 
# Its a best practice for computer programmers! 
# Notice the code above does it's best to avoid
# repeating values and code that has already 
# been written! 

# Below are the lyrics to Smokestack Lightnin' by Howlin Wolf
# Using the example above how could you break the lines below 
# into variables. Use the + and * operators to 

# There is a lot of repetition in the lyrics below
# your goals is to use code to avoid the repeating
# code that you have already written! 

"""
Ah oh, smokestack lightnin'
Shinin' just like gold
Why don't ya hear me cryin'?
A whoo hoo, whoo hoo, whoo

Whoa oh tell me, baby
What's the matter with you?
Why don't ya hear me cryin'?
Whoo hoo, whoo hoo, whooo

Whoa oh tell me, baby
Where did ya, stay last night?
A-why don't ya hear me cryin'?
Whoo hoo, whoo hoo, whoo

Whoa oh, stop your train
Let her go for a ride
Why don't ya hear me cryin'?
Whoo hoo, whoo hoo, whoo
"""

# Challenge: Define some variables for each line of the lyrics above
why = "Why don't ya hear me cryin'?"
whoo = "A whoo hoo, whoo hoo, whoo"
tell_me = "Whoa oh tell me, baby"

line_1 = "Ah oh, smokestack lightnin"
line_2 = "Shinin' just like gold"
line_3 = why
line_4 = whoo

line_5 = tell_me
line_6 = "What's the matter with you?"
line_7 = why
line_8 = whoo

line_9 = tell_me
line_10 = "Where did ya, stay last night?"
line_11 = "A-" + why.lower()
line_12 = whoo

line_13 = "Whoa oh, stop your train"
line_14 = "Let her go for a ride"
line_15 = why
line_16 = whoo

# Challenge: Print the song below
print(f"""
{line_1}
{line_2}
{line_3}
{line_4}

{line_5}
{line_6}
{line_7}
{line_8}

{line_9}
{line_10}
{line_11}
{line_12}

{line_13}
{line_14}
{line_15}
{line_16}
      """)