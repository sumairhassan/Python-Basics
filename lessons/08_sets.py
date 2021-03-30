# sets discarded duplicate values

def belt_count(dictionary):
    belts = list(dictionary.values())
    for belt in sets(belts):
        num = belts.count(belt)
        print(f'There are {num} {belt} belts')


ninja_belts = {} # creating the dictionaries

while True: # taking key-vlaue form user
    ninja_name = input('enter my name: ')
    ninja_color = input('enter my color: ')
    ninja_belts[ninja_name] = ninja_color # added the key-value to the dictionary

    another = input('another input? (y/n)') # adding another belt
    if another == 'y':
        continue # go back to the top of the loop and start again
    else:
        break

belt_count(ninja_belts)

