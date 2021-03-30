# double prizes money weekend

prizes = [5,10,15,20,25,50,100]

dbl_prizes = []

for prize in prizes:
    dbl_prizes.append(prize*2)
print(dbl_prizes)

# comprehension method

dbl_prizes = [prize*2 for prize in prizes]
print(dbl_prizes)

# squaring even numbers

nums = [1,2,3,4,5,6,7,8,9,10]

squared_even_nums = []

for num in nums:
    if(num%2)==0:
        squared_even_nums.append(num**2)
print(squared_even_nums)

# comprehension

squared_even_nums = [num**2 for num in nums if (num%2)==0]
print(squared_even_nums)