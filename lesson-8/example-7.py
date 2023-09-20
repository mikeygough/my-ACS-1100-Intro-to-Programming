'''
Let's practice writing to a file using .writelines()!

.writelines() writes a list of lines to the file. 

Each line must be a string!
'''

# STEP 1: Store file name in a variable
output_file_name = 'output.txt'

# STEP 2: Open the file in write mode ('w')
outfile = open(output_file_name, "w")

# STEP 3: Write list of the football teams stored in teams to the file.

teams = [
"Atlanta Falcons\n",
"Baltimore Ravens\n",
"Carolina Panthers\n",
"Green Bay Packers\n",
"Kansas City Chiefs\n",
"Los Angeles Chargers\n",
"Los Angeles Rams\n",
"Oakland Raiders\n",
"Philadelphia Eagles\n",
"Pittsburgh Steelers\n",
"San Francisco 49ers\n",
"New England Patriots\n"
]

# outfile.write('Philadephia Eagles')
outfile.writelines(teams)

# STEP 4: Close the file (We will learn about this the next few slides!)
outfile.close()