# Задание 2
# Создайте список целых чисел. Получите список квадратов нечётных чисел из этого списка.


def get_square(lst):
    odd_num = list(filter(lambda x: x % 2, lst))
    _square = list(map(lambda x: x ** 2, odd_num))
    return _square


lst = [5, 4, 13, 16, 20, 3, 8, 11]
print(get_square(lst))



# Задание 3
# Создайте функцию-генератор чисел Фибоначчи. Примените к ней декоратор, который будет 
# оставлять в последовательности только чётные числа.



def dec_fib(fn):
    
    def local_func(x):
        lst = []
        for i in fn(x):
            lst.append(i)
        even_num = list(filter(lambda x: x % 2 == False, lst))

        return even_num
        
    return local_func


@dec_fib
def fib(x):
    first, second = 0, 1
    for _ in range(x):
        yield second
        first, second = second, first + second

a = fib(30)
print(a)

