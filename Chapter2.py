spam = True;
apple = False;

print('42 == \'42\' evaluates to ' + str(42 == '42'))

# if statements
name = 'Mary'
password = 'swordfish'
if name == 'Mary':
    print ('Hello, Mary')
    if password == 'swordfish':
        print('Access granted')
    elif name == 'John': # in this case never executes
        print('You are John not Mary!')
    else:
        print ('Wrong password')

# while statement
count = 0
while count < 5:
    print('Hello!')
    count+=1

# break statement
while True:
    print('Please type your name:')
    name = input()
    if name == 'your name':
        break
print ('thank you')

# continue statement
while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello Joe, what is your password? ocean fish')
    password = input()
    if password == 'swordfish':
        break
print('Access granted')

# for loop and range
print('My name is')
for i in range(5):
    print('Jimmy McGill Five Times (' + str(i) + ')')

# exercise question 13
for i in range(0,10):
    print(i+1)
    
print()
index = 0
while index < 10:
    index = index + 1
    print(index)

# execise question 14
#spam.bacon()