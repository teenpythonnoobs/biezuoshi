import game

al_game = game.MyGame()

while al_game.again:

    if al_game.isNotWinAndNotLose():
        print('平手')
        al_game.again = False
    else:
        if al_game.guess_thing == 'scissors' and al_game.user_input_ok_thing == 'stone':
            al_game.whenWin()
        elif al_game.guess_thing == 'paper' and al_game.user_input_ok_thing == 'scissors':
            al_game.whenWin()
        elif al_game.guess_thing == 'stone' and al_game.user_input_ok_thing == 'paper':
            al_game.whenWin()
        else:
            if al_game.user_input_ok_thing != 'exit':
                print('you lose')
            al_game.again = False

''' if ((al_game.guess_thing == 'scissors' and al_game.user_input_ok_ting == 'stone') or (
                al_game.guess_thing == 'paper' and  al_game.user_input_ok_ting == 'scissors')  or (
                al_game.guess_thing == 'stone' and al_game.user_input_ok_thing == 'paper') ):
'''
