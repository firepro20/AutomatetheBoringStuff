import random

def hello():
    print('Hello mate!')


hello()

def helloUser(name):
    print('Hello ' + str(name)) # variables that have arguments assigned to them are parameters. name is a parameter of the helloUser function

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

print('Hello', end='') # by default the print() function always add a new line at the end. supplying the end argument to print function can change this behaviour
print('World') # will be added / concatinated with Hello

# similarly, multiple string values passed to print() will be automagically separated
print('cats', 'dogs', 'rabbits')