import glob


# Get all the text files from current directory
files = glob.glob('*.txt') # if want to read from other directory user glob.glob("<path to directory>.txt")


#Print content of first file and ignore all others
with open(files[0], 'rt') as fd:
    print (fd.read())