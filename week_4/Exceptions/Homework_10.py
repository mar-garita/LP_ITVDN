
# 1. Калькулятор с обработкой исключений. Запрашивает данные до тех пор пока не будет
# введено 'exit'. Реализует 3 функции на ваш выбор. Программа должна останавливаться
# только в случае 'exit '

def addition(x, y):
    result = x + y
    return result

def division(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        return "Division by zero"

def exponentiation(x, y):
    try:
        result = x ** y
        return result   
    except ZeroDivisionError:
        return 'Zero cannot be raised to a negative power'

def calculator():
    while True:
        options = input('Choose the option (1 calculator, 2 exit): ')
        if options == '1':
            number1 = int(input('Enter number1: '))
            number2 = int(input('Enter number2: '))
            operation = input('Choose an operation (+, /, **): ')

            if operation == '+':
                result_operation = addition(number1, number2)
                print(result_operation)
            elif operation == '/':
                result_operation = division(number1, number2)
                print(result_operation)
            elif operation == '**':
                result_operation = exponentiation(number1, number2)
                print(result_operation)
            else:
                print('Invalid operation')
        else:
            break
       
# calculator()


# 2. Создайте класс Editor, который содержит методы view_document и edit_document. 
# Создайте исключение. Пусть метод edit_document вызывает ваше исключение с текстом 
# ошибки доступа. Создайте подкласс ProEditor, в котором данный метод будет переопределён.
# Введите с клавиатуры лицензионный ключ и, если он корректный, создайте
# экземпляр класса ProEditor в противном случаеEditor(с помощью try/except/else).
# Вызовите методы просмотра и редактирования документов.

class MyExcept(Exception):
    pass


class Editor:

    def view_document(self):
        print('The documents is available for vieweing')

    def edit_document(self):
        try:
            raise MyExcept
        except MyExcept:
            print('Access error')
            print('Document editing is not available for the free version')


class ProEditor(Editor):

    def edit_document(self):
        print('The documents is available for editing')


def chek_key():
    try:
        key = int(input('Enter the license key: '))
    except ValueError:
        print('ValueError')
        print('Please enter a namber')
    else:
        if key == 123:
            obj = ProEditor()
                
        else:
            obj = Editor()
                
    return obj.edit_document()

chek_key()




