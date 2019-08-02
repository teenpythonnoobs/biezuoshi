import random


def randThing(shit):
    shit.guess_thing = random.choice(['scissors', 'stone', 'paper'])


def GetThing(shit):
    shit.user_input = input('please input something\n')
    if shit.user_input == 'scissors' or shit.user_input == 'stone' or shit.user_input == 'paper':
        shit.user_input_ok = shit.user_input
        shit.ok = True
    else:
        shit.ok = False
