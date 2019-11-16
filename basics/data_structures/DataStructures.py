

# Lists
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v) # will print index and value

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
#What is your name?  It is lancelot.
#What is your quest?  It is the holy grail.
#What is your favorite color?  It is blue.

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')
fruits.count('tangerine')
fruits.index('banana')
fruits.index('banana', 4)  # Find next banana starting a position 4
fruits.reverse()
fruits.sort()

# Tuple
t = 12345, 54321, 'hello!'
t.index(12345)
# print(t.index(123455)) ValueError
t.count('hello!')

# Set
fruits = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
vegetables = {'tomato', 'onion', 'cabbage', 'carrot'}
fruits.difference(vegetables) # Returns a set containing the difference between two or more sets
fruits.difference_update(vegetables) # Removes the items in this set that are also included in another, specified set
fruits.isdisjoint(vegetables) # Returns whether two sets have a intersection or not

a = set('abba')
b = set('azzmk')

print(a - b) # in a but not in b
print(a | b) # letters in a or b or both
print(a & b) # letters in both a and b
print(a ^ b) # letters in a or b but not both



