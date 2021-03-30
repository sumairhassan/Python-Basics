grades = ['A', 'B', 'B', 'E', 'C', 'C', 'C']

def remove_fails(grade):
    return grade!='E'

# by using filter function
print(list(filter(remove_fails, grades)))

# by using for loop

filtered_grades = []
for grade in grades:
    if grade != 'E':
        filtered_grades.append(grade)
print(filtered_grades)

# by using comprehension
print( [grade for grade in grades if grade != 'E'] )