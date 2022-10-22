""" Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь,
в котором каждый элемент списка является и ключом и значением.
Предполагается, что элементы списка будут соответствовать правилам задания ключей в словарях. """

""" def to_dict(some_list):
return {el: el for el in some_list}

some_list = [1, 'gghfty', 2.6]
print(to_dict(some_list)) """

""" 2. Иван решил создать самый большой словарь в мире.
Для этого он придумал функцию biggest_dict(**kwargs),
которая принимает неограниченное количество параметров «ключ: значение»
и обновляет созданный им словарь my_dict, состоящий всего из одного элемента
«first_one» со значением «we can do it». Воссоздайте эту функцию. """

""" my_dict = {'first_one': 'we can do it'}
def biggest_dict(**kwargs):
    my_dict.update(**kwargs)
print(my_dict) """

""" 3. Дана строка в виде случайной последовательности чисел от 0 до 9.
Требуется создать словарь, который в качестве ключей будет принимать данные числа
(т. е. ключи будут типом int), а в качестве значений – количество этих чисел в имеющейся
последовательности. Для построения словаря создайте функцию count_it(sequence),
принимающую строку из цифр.
Функция должна возвратить словарь из 3-х самых часто встречаемых чисел. """

""" from collections import Counter
def count_it(sequence):
     return dict(Counter([int(num) for num in sequence]).most_common(3))
print(count_it('987654321')) """

""" 4.Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки
в формате  «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий,
а значения — словари, реализованные по схеме предыдущего задания
и содержащие записи, в которых фамилия начинается с соответствующей буквы.
Например:
>>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
{"А": {"П": ["Петр Алексеев"]},"И": {"И": ["Илья Иванов"]},"С": {"И": ["Иван Сергеев", "Инна Серова"],
"А": ["Анна Савельева"]}} """

""" lst = ["Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"]

def fam(lst):
        some_dict = {}
        for item in lst:
ind = item.index(' ') + 1
if item[ind] in some_dict:
            some_dict[item[ind]].append(item)
else:
        some_dict[item[ind]] = [item]
return some_dict

def name(lst):
        some_dict = {}
for item in lst:
        if item[0] in some_dict:
some_dict[item[0]].append(item)
else:
some_dict[item[0]] = [item]
return some_dict

def thesaurus_adv(lst):
        temp_dict = fam(lst)
result = {}
for key in temp_dict.keys():
        result[key] = name(temp_dict[key])
return result
print(f' Получившийся словарь -', thesaurus_adv(lst)) """