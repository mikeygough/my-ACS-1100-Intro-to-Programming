with open("somefile.txt", "a") as outfile:
  mytext = ['something\n', 'to\n', 'say']
  outfile.writelines(mytext)