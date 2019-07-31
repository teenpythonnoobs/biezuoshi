import random


def randthing(shit):
    shit.guessthing = random.choice(['scissors', 'stone', 'paper'])


def getthing(shit):
    shit.userinput = input('please input something')
    if shit.userinput == 'scissors' or shit.userinput == 'stone' or shit.userinput == 'paper':
        shit.userinputok = shit.userinput
        shit.ok = 0
    else:
        shit.ok = 1
