# lambdas are like analymous function, which dont need name or anyi dentifier
# which only ever used ones

nums = [1,2,3,4,5,6]

def square(n): # if we are only using once, we dont need to define a name forward
    return n*n

#print(list(map(square, nums)))

#lambda n: n*n
#using lambda

print(list(map(lambda n:n*n, nums)))

# lambdas are basically ananymous inline functions and they are good when we use a particular function once