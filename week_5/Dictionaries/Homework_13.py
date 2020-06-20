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


def add_link(d_links): 
    while True:
        link = input('Write a link: ')
        short_link = input('Write a short link: ')
        d_links[short_link] = link
        option = input('Enter 1 (Add another link) or 2 (Exit): ')
        if option == '2':
            break
    return d_links

def get_link(d_links):   
    key = input('Enter a short link: ')  
    if key in d_links: 
        link = d_links[key]
    else:
        raise KeyError
    return link
    

def work_links():
    dict_links = {}

    dict_links = add_link(dict_links)  
    print(dict_links)   

    link = get_link(dict_links)

    return link

print(work_links())