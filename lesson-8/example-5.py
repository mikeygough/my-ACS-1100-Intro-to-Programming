'''
Function Practice: 

modify the code you just wrote by 
creating a function called read_candy() 
that takes in the file name as a parameter 
and returns the lines of the file as a list
'''

# STEP 1: Store the name of the file
# TODO: define a variable filename and store the name 
# of the file cand.txt. Ask yourself what the path 
# should be? 


def read_lines(filename):
  # Open
  infile = open(filename, 'r')

  # Read
  lines = infile.readlines()

  #Close
  infile.close()

  # Return
  return lines

#TODO: print out all the lines of the candy file
candy_lines = read_lines('candy.txt')
print(candy_lines)