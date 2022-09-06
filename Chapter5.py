import pprint
spam = {'name':'Zophie', 'age':'19'}
# spam['color'] # will result in a key error as key does not exist

for v in spam.values():
    print(v)

for k in spam.keys():
    print(k)
print("\n")
for i in spam.items():
    print(i)

print('name' in spam.keys())

print('name' in spam) # this is a shortcut for the above, means check for keys

print('surname' not in spam)
print('Zophie' in spam.values())

picnicItems = {'apples': 5, 'cups': 2}
print('I am bringing ' + str(picnicItems.get('apples', 0)) + ' cups.')
print('I am bringing ' + str(picnicItems.get('states', 0)) + ' cups.')

picnicItems.setdefault('tools', '10') #checking for a key and setting to a value in one line

message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

# counts each character appearance in the string
# print(count)
pprint.pprint(count)

allGuests = {'Alice': {'apples': 5, 'pretzels': 12},
             'Bob': {'ham sandwiches': 3, 'apples': 2},
             'Carol': {'cups': 3, 'apple pies': 1}}



def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
       numBrought = numBrought + v.get(item, 0)
    return numBrought


print('Number of things being brought:')
print(' - Apples         ' + str(totalBrought(allGuests, 'apples')))
print(' - Cups           ' + str(totalBrought(allGuests, 'cups')))
print(' - Cakes          ' + str(totalBrought(allGuests, 'cakes')))
print(' - Ham Sandwiches ' + str(totalBrought(allGuests, 'ham sandwiches')))
print(' - Apple Pies     ' + str(totalBrought(allGuests, 'apple pies')))



# Practice Questions 

# 1. dictionarySample = {}
# 2. dictionarySample = {'foo':'42'}
# 3. A list is ordered while a dictionary is not.
# 4. A Key error will be printed and an exception is raised
# 5. Essentially the same, both check if key exists
# 6. One checks for keys, the other for a key value
# 7. spam.setdefault('color', 'black')
# 8. pprint