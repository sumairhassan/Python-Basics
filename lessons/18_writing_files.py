# by default open function is in read only mode, so we need to pass extra perimeter

with open('files/write.txt', 'w') as write_file:
    write_file.write('Python is awesome.')
    write_file.write('\nPython is awesome awesome.')

# later on outside of this code block
# some code and then

#with open('files/write.txt', 'w') as write_file:
#    write_file.write('adding extra line.') # it will over write the file and start from the beginning.
# we will pass 'a' instead of 'w'. a = ammend.

with open('files/write.txt', 'a') as write_file:
    write_file.write('\nadding extra line.')


quotes = [
    '\n'
    '\nline number 1',
    '\nline number 3',
    '\nline number 3',
    '\nline number 4'
]

with open('files/write.txt', 'a') as write_file:
    write_file.writelines(quotes)