class Button:


    def __init__(self, text, link):
        self.text = text
        self.link = link

home = Button('Домой', '/home')
catalog_msk = Button('Каталог', '/msk/catalog')

print(home.text)
print('Кнопка', home.text, 'имеет ссылку', home.link)

print('\n')

print(catalog_msk.text)
print('Кнопка',  catalog_msk.text, 'имеет ссылку', catalog_msk.link)

class ButtonTwo:
    def __init__(self, text, link, loc):
        self.text = text
        self.link = link
        self.loc = loc

    def click(self):
        return "Клик по локатору - {}".format(self.loc)

home_two = ButtonTwo('Домой', '/home', 'button#home')

print(home_two.click())

class Input:
    def __init__(self, loc):
        self.loc = loc
search = Input('search#input')

print(search.loc)

class Page:
    def __init__(self, url):
        self.url = url
    def get(self):
        print(self.url)
home = Page('home#page')
home.get()

class Soda:
    def __init__(self, ing=None):
        self.ing = ing
    def show_my_drink(self):
        if self.ing:
            print(f'Газировка и {self.ing}')
        else:
            print("Обычная газировка")
drink1 = Soda()
drink2 = Soda('Малина')

drink1.show_my_drink()
drink2.show_my_drink()

#Наследование классов

class Mammal:
    className = 'Млекопитающие'

class Dog(Mammal):
    species = 'Canis lupus'

dog = Dog()
print(dog.className)

