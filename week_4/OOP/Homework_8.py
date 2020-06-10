# Задание 1
# Создайте класс, описывающий книгу. Он должен содержать информацию об авторе, 
# названии, годе издания и жанре. Создайте несколько разных книг. Определите 
# для него операции проверки на равенство и неравенство, методы __repr__ и __str__.

# Задание 2
# Создайте класс, описывающий отзыв к книге. Добавьте в класс книги поле – список отзывов.
# Сделайте так, что при выводе книги на экран при помощи функции print также будут 
# выводиться отзывы к ней.


class Review: 
    def __init__(self, title, review = ''):
        self.title = title
        self.review = review  

    def make_review(self):
        if self.title == 'Idiot':
            self.review = 'Great book'
            
        elif self.title == 'Player':
            self.review = 'Good book'
        elif self.title == 'Warm Heart':
            self.review = 'Very good book'
    
        return self.review

        
class Book(Review):
    def __init__(self, title, author = '', publication_date = 0, style = '', review = ''):
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.style = style 
        self.review = review

    @property
    def get_information(self):
        if self.title == 'Idiot':
            self.author = 'Dostoevsky'
            self.publication_date = 1868
            self.style = 'novel'
            self.review = Review.make_review(self)
        elif self.title == 'Player':
            self.author = 'Dostoevsky'
            self.publication_date = 1866
            self.style = 'novel'
            self.review = Review.make_review(self)
        elif self.title == 'Warm Heart':
            self.author = 'Ostrovsky'
            self.publication_date = 1866
            self.style = 'comedy'
            self.review = Review.make_review(self)
     
        return self.author, self.publication_date, self.style, self.review

    def _eq_(self, other):
        return self is other

    def __str__(self):
        self.get_information
        return 'Book title: {}, author: {}, publication date: {}, style: {}, review: {}'.format(self.title, self.author, self.publication_date, self.style, self.review)


book1 = Book('Idiot')
book2 = Book('Player')
book3 = Book('Warm Heart')

print(book1)
print(book2)
print(book3)

print(book1 == book2)
print(book1 == book3)
print(book1 == book1)



# Задание 3
# Используя ссылки в конце данного урока, ознакомьтесь с таким средством инкапсуляции 
# как свойства. Ознакомьтесь с декоратором property в Python. Создайте класс, описывающий 
# температуру и позволяющий задавать и получать температуру по шкале Цельсия и Фаренгейта, 
# причём данные могут быть заданы в одной шкале, а получены в другой.
 


class Temperature:

    def __init__(self, temperature, degree):
        self.temperature = temperature
        self.degree = degree
    
    @property
    def conversion(self):
        if self.degree == 'C':
            fahrenheit = (1.8 * self.temperature) + 32
            return '{}C = {}F'.format(self.temperature, fahrenheit)
        elif self.degree == 'F':
            celsius = (self.temperature - 32) / 1.8
            return '{}F = {}C'.format(self.temperature, celsius)
    

t1 = Temperature(-30, 'F')
t2 = Temperature(30, 'C')
print(t1.conversion) 
print(t2.conversion)

