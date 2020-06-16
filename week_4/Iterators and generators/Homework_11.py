# Задание 1
# Напишите итератор, который возвращает элементы заданного списка в обратном порядке (аналог reversed).

import math

class ReversRange:  

    def __init__(self, start, end=None):                 
        if end is None:                                          
            self.start = 0                                       
            self.end = start                                     
        else:                                                    
            self.start = start
            self.end = end
        self.lenght = math.ceil(self.end - self.start)  

    def __len__(self):                                              
        return self.lenght

    def __getitem__(self, item):                                  
        if 0 <= item < len(self):                                  
            return self.end - item                     
        else:
            raise IndexError('Too much')
       

for i in ReversRange(6):
    print(i)

for i in ReversRange(2, 7):
    print(i)



# Задание 2
# Перепишите решение первого задания с помощью генератора.

def func_rev(start, end=None):
    if end == None:
        for i in range(start):
            yield start 
            start -= 1   
    else:
        for i in range(start, end):
            yield end
            end -= 1


f = func_rev(6)   

for i in f:
    print(i) 


f = func_rev(2, 7)

for i in f:
    print(i)


         











   

