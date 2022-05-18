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