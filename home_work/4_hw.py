class Rectangle:

    def __init__(self, widht, height):
        self.widht = widht
        self.height = height

    def square(self):
        return self.widht * self.height

    def perimeter(self):
        return 2 * (self.widht + self.height)

rec1 = Rectangle(2, 3)
rec2 = Rectangle(5, 6)
rec3 = Rectangle(10, 20)
print(rec1.square())
print(rec2.square())
print(rec2.square())
print(rec1.perimeter())
print(rec2.perimeter())
print(rec3.perimeter())
print("\n")

class Math:

    def __init__(self, a, b):
        self.a = a
        self.b = b
    def addition(self):
        return self.a + self.b
    def multiplication(self):
        return self.a * self.b
    def division(self):
        return self.a / self.b
    def subtraction(self):
        return self.a - self.b

resultat = Math(20, 10)
print(resultat.addition())
print(resultat.multiplication())
print(resultat.division())
print(resultat.subtraction())

class Button:

    type: str = 'Кнопка'


    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

    def click(self):
        return  f"Клик по кнопке {self.text}"

Textbox = Button('Text Box', 'https://demoqa.com/text-box')
Checkbox = Button('Check box', 'https://demoqa.com/checkbox')
Radiobutton = Button('Radio button', 'https://demoqa.com/radio-button')
Webtables  = Button('Web tables','https://demoqa.com/webtables')
Buttons = Button('Buttons', 'https://demoqa.com/buttons')
Links = Button('Links', 'https://demoqa.com/links')
Broken_Link_Images = Button('Broken_Link_Images', 'https://demoqa.com/broken')
Upload_and_Download = Button('Upload_and_Download', 'https://demoqa.com/upload-download')
Dynamic_properties = Button('Dynamic_properties', 'https://demoqa.com/dynamic-properties')

print(Textbox.text)
print(Checkbox.text)
print(Radiobutton.text)
print(Webtables.text)
print(Buttons.text)
print(Links.text)
print(Broken_Link_Images.text)
print(Dynamic_properties.text)

print('\n')
print(Textbox.click())
print(Checkbox.click())
print(Radiobutton.click())
print(Webtables.click())
print(Buttons.click())
print(Links.click())
print(Broken_Link_Images.click())
print(Dynamic_properties.click())

# Доп*

class Car:

    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year
    def starting(self):
        print('Автомобиль заведен')
    def shutdown(self):
        print('Автомобиль заглушен')
    def manufacture(self):
        return self.year
    def type_car(self):
        return self.type
    def color_car(self):
        return self.color

car = Car('красный', 'пикап', '2024')

print(car.starting())
print(car.shutdown())
print(car.manufacture())
print(car.type_car())
print(car.color_car())