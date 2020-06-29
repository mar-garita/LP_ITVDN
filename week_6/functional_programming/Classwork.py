# 1. создайте словарь с основными арифметическими функциями

# Решение 1
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mult(x, y):
    return x * y

def div(x, y):
    if x == 0:
        raise ZeroDivisionError
    return x / y


dic1 = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}
a = dic1.get('add')
print(a(10, 12))


# Решение 2
dic2 = {
    'add': lambda x, y: x + y,
    'sub': lambda x, y: x - y,
    'mult': lambda x, y: x * y,
    'div': lambda x, y: x / y
}
a = dic2.get('sub')
print(a(8, 4))




# 2. Создайте функцию высшего порядка которая принимает значение
# и перемножает его с каждым значением из рандомного списка
# (сделайте это двумя способами(partial, ручками))

lst = [1, 2, 3, 4, 5]

# Решение 1
def func(x): 
    
    def func1(lst):
        y = 1
        for i in lst:
            y = y * i
        return x * y

    return func1

a = func(10)(lst)  
print(a)


# Решение 2
from functools import reduce

def func(x): 
    
    def func1(lst):
        b = reduce(lambda x, y: x * y, lst) 
        return b * x

    return func1

a = func(10)(lst)  
print(a)




# 3. создайте 2 функция:
#     - принимает число и выводит его на печать
#     - принимает имя и выводит его на печать
#    создайте декоратор который будет выводить приветствие

def func_dec(fn):

    def greeting(*args):
        print('Hello!')
        a = fn(*args)
        return a

    return greeting

@func_dec
def number(x):
    print(x)


@func_dec
def name(string):
    print(string)
    

number(10)

name('Rita')




# 4. возведите каждый елемент списка в третью степень одной строкой
# (2 способа)(генератор списка)

lst = [1, 2, 3, 4, 5, 6]

# Решение 1
a = list(map(lambda x: x ** 3, lst))
print(a)

# Решение 2
a = [i ** 3 for i in lst]
print(a)