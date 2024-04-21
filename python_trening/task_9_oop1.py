#Задание 5

from task_9_checks import Checks

class Input(Checks):
    def __init__(self, loc):
        super().__init__(loc)
        self.loc = loc
search = Input('search#input')

print(search.check_text())

class Button(Checks):
    def __init__(self, loc):
        super().__init__(loc)
        self.loc = loc


search = Button('search#button')

print(search.check_text())

class Title(Checks):
    def __init__(self, loc):
        super().__init__(loc)
        self.loc = loc


search = Title('search#title')

print(search.check_text())

class Link(Checks):
    def __init__(self, loc):
        super().__init__(loc)
        self.loc = loc


search = Link('search#link')

print(search.check_text())



