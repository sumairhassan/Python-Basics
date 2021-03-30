###################### Basic Function #####################
"""
def greet():
    print('Hello World')

greet()
greet()
greet()"""

################# Passing parameters ########################
"""
def greet(name, time):
    print(f'Good {time} {name}, hope you are well')

greet('Sumair', 'morning')"""

############# Taking input from user and passing as arguments #########
"""
def greet(name, time):
    print(f'Good {time} {name}, hope you are well')

name = input('Enter the name: ')
time = input('Enter the time: ')

greet(name, time)"""

############# Default input/argument, in case of argument missing #######
"""
def greet(name='Sumair', time='Morning'):
    print(f'Good {time} {name}, hope you are well')

#name = input('Enter the name: ')
#time = input('Enter the time: ')

#greet()
#greet(name = 'Hassan') # this will over write the parameter
greet('Hassan', 'Afternoon')"""

######### Taking input from user, with also have default argument ######
"""
def greet(name='Sumair', time='Morning'):
    print(f'Good {time} {name}, hope you are well')

name = input('Enter the name: ')
time = input('Enter the time: ')

greet(name, time)"""

######################################################
######################################################
######### Area of Circle
#####################################################
"""
def area(radius):
    print(3.14*radius*radius)

area(5)"""

#### Asking radius/input from  user ###
"""
def area(radius):
    print(3.14*radius*radius)

radius = int(input('enter the radius: '))

area(radius)"""

######## calculating volume of cylynder

def area(radius):
    return 3.14*radius*radius

def volume(area, length):
    print(area*length)

radius = int(input('enter the radius: '))
length = int(input('enter the volume: '))

#area_calc = area(radius)
#volume(area_calc, length)

volume(area(radius), length) # passing function into fnction as a parameter

