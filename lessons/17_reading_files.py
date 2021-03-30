"""

ipsum_file = open('files/ipsum.txt') # open the file

# using for loop method

for line in ipsum_file:
    #print(line)
    # if we want to remove gap between lines,we can use method rstrip
    print(line.rstrip())

# another way

# readlines will read the content of file and each line is going to be stored
# as an elements, a string in list.

ipsum_file.seek(0)

lines = ipsum_file.readlines()
print(lines) 
# this will give the empty string because cusror is in the end due to for loop method,
# we have already read that file.
# to reset the cursor we will use method .seek method (0) will start from 0 location

# one more method

ipsum_file.seek(50) # reading 100 character from that point
file_text = ipsum_file.read(100)
print(file_text)

ipsum_file.close() # closing the file. File must be closed after that.

"""

#####################################################################

# different way to do it. we dont need close method in this

def sequence_filter(line):
    return '>' not in line # removing > sequence line

with open('files/dna_sequence.txt') as dna_file:
    lines = dna_file.readlines()
    #filter(sequence_filter, lines) # also need type casting here
    print(list(filter(sequence_filter, lines))) 

# carry on, this file with automatically close

    



