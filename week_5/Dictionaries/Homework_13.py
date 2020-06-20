# Задание 1
# Даны две строки. Выведите на экран символы, которые есть в обоих строках.

first = ('hello')
second = ('world')

common_element = set(first) & set(second)

print(common_element)


# Задание 2
# Создайте программу, которая эмулирует работу сервиса по сокращению ссылок. 
# Должна быть реализована возможность ввода изначальной ссылки и короткого 
# названия и получения изначальной ссылки по её названию.


def work_links():
    
    def add_link():     # Функция принимает ссылки и их короткие названия, и сохраняет в словарь
        dict_links = {}
        while True:
            option = input('Enter 1 to write the link or 2 to exit: ')
            if option == '1':
                link = input('Write a link: ')
                short_link = input('Write a short link: ')
                dict_links[short_link] = link
            else:
                break
        return dict_links

    dict_links = add_link()  # Получила словарь, в который ввела ссылки
    print(dict_links)        # print напечатала чтобы видеть, что словарь с ссылками есть

    def get_link():     # Функция выдает ссылку по ее короткому названию
        key = input('Enter a short link: ')
        link = dict_links[key]
        return link
    
    link = get_link()

    return link

print(work_links())