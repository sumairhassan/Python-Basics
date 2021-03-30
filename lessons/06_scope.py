"""
my_name = 'Sumair'

def print_name():
    print('the name inside the function ', my_name)

print_name()
print('the name outside the function ', my_name)"""

"""
my_name = 'Sumair'

def print_name():
    my_name = 'Hassan' # local scope
    print('the name inside the function ', my_name)

print_name()
print('the name outside the function ', my_name)"""


my_name = 'Sumair'

def print_name():
    global my_name # global scope
    my_name = 'Hassan'
    print('the name inside the function ', my_name)

print_name()
print('the name outside the function ', my_name)  