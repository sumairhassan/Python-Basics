# dictionaties are data types like json format key-value pair

def ninja_intro(dictionary): # cycle through, what the user entered. The fuction will output the deatils
    for key, val in dictionary.items():
        print(f'I am {key} and I am a {val} belt')


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

ninja_intro(ninja_belts) # calling the function once we exited fromthe loop

