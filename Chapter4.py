import random


spam = ['cat', 'bat', 'rat', 'elephant']
print(spam[:2])
print(spam[1:])
spam[:]
print(spam[-3:-1]) # -1 is the same as last index

print(len(spam))

spam[1] = 'test'
print(spam)

# Concatenation and Replication
print([1,2,3] + ['A','B','C'])
print(['X', 'Y', 'Z'] * 3) 

# deleting values from a list
del spam[2]
print(spam)
del spam[2]
print(spam)

# working with lists
catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) +
      ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]  # list concatenation
print('The cat names are:')
for name in catNames:
    print('  ' + name)

# Loops with lists
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

# In and not in operators for lists
# similar to contains in C# Linq possibly
# search by value not index (C++ at function)
spam = ['hello', 'hi', 'howdy', 'heyas']
'cat' in spam # output false
'tiger' not in spam # output true

# Loops with lists using enumerate()
supplies = ['pens', 'staplers', 'flamethrowers', 'binders']
for index, item in enumerate(supplies):
    print('Index ' + str(index) + ' in supplies is: ' + item)

# Random Choice and Random Shuffle
random.choice(supplies)
random.shuffle(supplies)
print(supplies)

# Method
supplies.index('pens')
supplies.append('papers') # end of list
supplies.insert(1, 'paperclips') # at the index
supplies.remove('pens')

supplies.sort(reverse=True)

# Character Picture Grid Exercise
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

#cols = []
#print(len(grid))
#print(len(grid[0]))
for i in range(len(grid[0])):
    for j in range(len(grid)):
        print(grid[j][i], end='')
    print('\n')

# Questions for Chapter 4
# 1. What is []? - an empty list
# 2. How would you assign the value 'hello' as the third value in a list stored in a variable named spam? 
# Assume spam contains ([2,4,6,8.10]) -  spam[2] = 'hello'
# 3. d 
# 4. d
# 5. a b // excluding :2
# 6. 1
# 7. [3.14, 'cat', 11, 'cat', True, 99
# 8. [3.14, 11, 'cat', True, 99]
# 9. + * // question asked for operators
# 10. appends add items at the end of the list; 
# insert adds an item at index location
# 11. del list[index] / list.remove(value)
# 12. They both can be concatenated and replicated
# sequences of data. ask for character via index
# string can be accessed same way as list. string is a list of characters
# in function works on lists and strings
# 13. list are mutable and tuple are immutable
# 14. mytuple = (42,)
# 15. typecasting tuple(listvalue) / list(tuplevalue)
# 16. references
# 17. copies first layer of values, deepcopy copies lists within lists