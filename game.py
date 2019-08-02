import functions


class MyGame:
    def __init__(self):
        self.guess_thing = self.user_input = self.user_input_ok_thing = ''

        functions.randThing(self)
        self.user_input_ok_or_not = False
        while not self.user_input_ok_or_not:
            functions.GetThing(self)
        self.again = True

    def isNotWinAndNotLose(self):
        if self.guess_thing == self.user_input:
            return True
        else:
            return False

    def whenWin(self):
        if functions.Again():
            functions.randThing(self)
            self.user_input_ok_or_not = False
            while not self.user_input_ok_or_not:
                functions.GetThing(self)
            self.again = True
        else:
            self.again = False
