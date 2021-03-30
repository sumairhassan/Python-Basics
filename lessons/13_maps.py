from random import shuffle

def jumble(word):
    anagram = list(word)
    shuffle(anagram)
    return "".join(anagram)

words = ['beetroot', 'carrots', 'potatoes']
anagrams = []

# way of doing with for loop.
for word in words:
    anagrams.append(jumble(word))
print(anagrams)

# map function
# map(function, data)
# way of doing with map function

print(list(map(jumble, words)))

# way of doing with comprehension

print( [jumble(word) for word in words] )