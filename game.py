import functions


class MyGame:
    def __init__(self):
        self.guess_thing = self.user_input = self.user_input_ok = ''

        functions.randThing(self)
        self.ok = False
        while not self.ok:
            functions.GetThing(self)
