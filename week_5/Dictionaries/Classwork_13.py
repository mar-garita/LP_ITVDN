# 1. Создайте словарь, связав его с переменной school, и наполните данными,
# которые бы отражали количество учащихся в разных классах (1а, 1б, 2б, 6а, 7в и т. п.).
# Внесите изменения в словарь согласно следующему: а) в одном из классов изменилось
# количество учащихся, б) в школе появился новый класс, с) в школе был расформирован
# (удален) другой класс. Вычислите общее количество учащихся в школе.

school = {'1a': 20, '1b': 21, '2a': 32, '2b': 24, '3a': 17, '3b': 19}

print(school)

school['2a'] = 25
print(school)

school['4a'] = 23
print(school)

school.pop('1b')
print(school)

lst_val = [school.get(key) for key in school]
all_students = sum(lst_val)
print(all_students)


# 2. Создайте словарь, где ключами являются числа, а значениями – строки.
# Примените к нему метод items(), полученный объект dict_items
# передайте в написанную вами функцию, которая создает и
# возвращает новый словарь, "обратный" исходному, т. е.
#  ключами являются строки, а значениями – числа.


my_dict = {
    1: 'val1',
    2: 'val2',
    3: 'val3',
    4: 'val4',
    5: 'val5'
}

print(my_dict)


def change_dict(d):
    new_dict = {}
    for key, val in d.items():
        key, val = val, key
        new_dict[key] = val
        
    return new_dict   
              
print(change_dict(my_dict))