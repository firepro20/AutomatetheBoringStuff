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
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
print('I am bringing ' + str(picnicItems.get('states', 0)) + ' cups.')