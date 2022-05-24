import random


def hello():
    print('Hello mate!')


hello()


def helloUser(name):
    # variables that have arguments assigned to them are parameters. name is a parameter of the helloUser function
    print('Hello ' + str(name))


helloUser('22')


def getAnswer(answerNumber):
       if answerNumber == 1:
           return 'It is certain'
       elif answerNumber == 2:
           return 'It is decidedly so'
       elif answerNumber == 3:
           return 'Yes'
       elif answerNumber == 4:
           return 'Reply hazy try again'
       elif answerNumber == 5:
           return 'Ask again later'
       elif answerNumber == 6:
           return 'Concentrate and ask again'
       elif answerNumber == 7:
           return 'My reply is no'
       elif answerNumber == 8:
           return 'Outlook not so good'
       elif answerNumber == 9:
           return 'Very doubtful'


r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)

# can also be shortened to print(getAnswer(random.randint(1,9))) ask if range is inclusive of start and end values

# by default the print() function always add a new line at the end. supplying the end argument to print function can change this behaviour
print('Hello', end='')
print('World')  # will be added / concatinated with Hello

# similarly, multiple string values passed to print() will be automagically separated
print('cats', 'dogs', 'rabbits')

# Functions


def a():
    print('a() starts')
    b()
    d()
    print('a() returns')

def b():
    print('b() starts')
    c()
    print('b() returns')

def c():
    print('c() starts')
    print('c() returns')

def d():
    print('d() starts')
    print('d() returns')

a()

# If you try to use a local variable in a function before you assign a value to it, as in the following program,
# Python will give you an error. 

""" def spam():
    
    print(eggs)
    eggs = 'spam local'
    
eggs = 'global'
spam() """

"""
This error happens because Python sees that there is an assignment statement 
for eggs in the spam() function and, therefore, considers eggs to be local. 
But because print(eggs) is executed before eggs is assigned anything, the 
local variable eggs doesn’t exist. Python will not fall back to using the global 
eggs variable.
"""

# Exception handling

def spam(divideBy):
	try:
		return 42/divideBy
	except ZeroDivisionError:
		print('Error: Invalid Argument.')
print(spam(2))
print(spam(12))
print(spam(0)) # returns None as default return value for a function
print(spam(1))

def spam(divideBy):
    return 42 / divideBy

try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('Error: Invalid argument.') # best way of doing it

# The Collatz Sequence

def collatz(number):
    if (number <= 0):
        return 1
    elif ((number % 2) == 0):
        print(number // 2)
        return number // 2
    elif((number % 2) == 1):
        print(3 * number + 1)
        return 3 * number + 1
    else:
        return 1
        
try:
    mynumber = int(input('Enter a number:'))
    output = 0
    while (mynumber != 1):
        output = collatz(mynumber)
        mynumber = output
except ValueError:
    print('The input was not a valid integer')