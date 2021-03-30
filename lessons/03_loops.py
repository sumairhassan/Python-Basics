# For loops

#ninjas = ['ryu', 'crystal', 'yashi', 'ken']

"""for ninja in ninjas:
    print(ninja)"""

#for ninja in ninjas[1:3]:
 #   print(ninja)

"""for ninja in ninjas:
    if ninja == 'yashi':
        print(f'{ninja} -- black belt')
    else:
        print(ninja)"""


"""for ninja in ninjas:
    if ninja == 'yashi':
        print(f'{ninja} -- black belt')
        break
    else:
        print(ninja)"""

######################################################################

# While loops

age=25
num=0

"""
while num<age:
    print(num)
    num +=1 """

# printing only even number
"""
while num<age:
    if(num%2==0):
        print(num)
    num+=1 """

# printing till num =10
"""
while num<age:
    if(num%2==0):
        print(num)
    if num>10:
        break
    num+=1 """

# dont want to output 0.
while num<age:
    if num==0:
        num+=1
        continue
    if(num%2==0):
        print(num)
    if num>10:
        break
    num+=1