import random


def randThing(shit):

    shit.guess_thing = random.choice(['scissors', 'stone', 'paper'])


def GetThing(shit):
    shit.user_input = input('输入stone/scissors/paper \n')
    if shit.user_input == 'scissors' or shit.user_input == 'stone' or shit.user_input == 'paper':
        shit.user_input_ok_thing = shit.user_input
        shit.user_input_ok_or_not = True
    elif shit.user_input == 'exit':

        shit.user_input_ok_or_not = True
    else :
        shit.user_input_ok_or_not = False


def Again():
    user_input = input('你赢了 ！！！！！！！ \n是否重来 y/n\n')
    if user_input == 'y':
        return True
    else:
        return False
