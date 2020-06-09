# Задание 1
# Создайте класс Editor, который содержит методы view_document и 
# edit_document. Пусть метод edit_document выводит на экран информацию 
# о том, что редактирование документов недоступно для бесплатной версии. 
# Создайте подкласс ProEditor, в котором данный метод будет переопределён. 
# Введите с клавиатуры лицензионный ключ и, если он корректный, создайте 
# экземпляр класса ProEditor, иначе Editor. Вызовите методы просмотра и 
# редактирования документов.

class Editor:

    def view_document(self):
        print('The documents is available for vieweing')

    def edit_document(self):
        print('Document editing is not available for the free version')


class ProEditor(Editor):

    def edit_document(self):
        print('The documents is available for editing')


def chek_key():
    key = input('Enter the license key: ')

    if key == '123':
        obj = ProEditor()
         
    else:
        obj = Editor()
                
    return obj.edit_document()

chek_key()


        


# Задание 2
# Опишите классы графического объекта, прямоугольника и объекта, который 
# может обрабатывать нажатия мыши. Опишите класс кнопки. Создайте объект 
# кнопки и обычного прямоугольника. Вызовите метод нажатия на кнопку.

class GraphicObject:
    pass
        
class Rectange(GraphicObject):
    pass

class PressingButton(): 
    def one_click(self):
        return 1

    def double_click(self):
        return 2

    def long_press(self):
        return 3

class Button(Rectange, PressingButton):
    pass

obj = Button()
print(obj.one_click())
print(obj.double_click())
print(obj.long_press())



# Задание 3
# Создайте иерархию классов с использованием множественного наследования. 
# Выведите на экран порядок разрешения методов для каждого из классов. 
# Объясните, почему линеаризации данных классов выглядят именно так.


class Product:

    def name(self, name):
        self.name = name
        return name

    def price(self, price):
        self.price = price
        return price

    def discount(self, discount):
        self.discount = discount
        if self.price > 1000:
            discount = self.price * discount / 100
        else:
            discount = 0
        return discount

    def color(self, color):
        self.color = color
        return color

class Monitor(Product):

    def diagonal(self, diagonal):
        self.diagonal = diagonal
        return diagonal

class SetTopBox(Product): 

    def tuner(self, tuner):
        self.ftuner = tuner
        return tuner
        
    def memory(self, memory):
        self.memory = memory
        return memory

class Television(Monitor, SetTopBox):

    def function_3d(self, function_3d):
        self.function_3d = function_3d
        return function_3d



tv = Television()
print(tv.name('Samsung'))
print(tv.price(2000))
print(tv.discount(10))
print(tv.color('Gold'))
print(tv.diagonal(108))
print(tv.tuner('+'))
print(tv.memory(512))
print(tv.function_3d('+'))


