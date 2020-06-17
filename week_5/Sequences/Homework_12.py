# Задание 1
# Создайте функцию от произвольного количества аргументов, которая 
# вычисляет среднее арифметическое данных чисел. Вычислите при помощи 
# неё среднее арифметическое двух заданных чисел и среднее 
# арифметическое чисел из заданного диапазона.


class MyExcept(Exception):
    pass

def my_func(*args):
    args = tuple(args)
    arith_mean_args = sum(args) / len(args)

    print('Calculate the arithmeric mean of two numbers')
    index1 = int(input('Enter the index of the first element: '))
    if index1 >= len(args):
        raise MyExcept('Invalid index')
    index2 = int(input('Enter the index of the second element: '))
    if index2 > len(args):
        raise MyExcept('Invalid index')
    f_element = args[index1]
    s_element = args[index2]
    arith_mean_fs = (f_element + s_element) / 2

    print('Calculate the arithmeric mean range')
    start = int(input('Enter the index of the first element: '))
    if index1 >= len(args):
        raise MyExcept('Invalid index')
    end = int(input('Enter the index of the second element: '))
    if index2 > len(args):
        raise MyExcept('Invalid index')
    r = args[start:end]
    arith_mean_r = sum(r) / len(r)

    return f"""Arithmetic mean of the args: {arith_mean_args}
Arithmetic mean of the element[{index1}] and element[{index2}]: {arith_mean_fs}
Arithmetic mean of the range[{start}:{end}]: {arith_mean_r}"""


x = my_func(2, 31, 6, 7, 2, 3, 4, 6, 17)
print(x)

 

# Задание
# Напишите программу, которая вводит с клавиатуры последовательность 
# чисел и выводит её отсортированной в порядке возрастания.

def sort_numbers():
    numbers = input('Enter numbers using spacebar: ').split()
    lst = list(map(int, numbers))
    lst.sort()

    return lst

print(sort_numbers())







