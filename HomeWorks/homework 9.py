# 1. Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь,
# в котором каждый элемент списка является и ключом и значением. Предполагается, что элементы списка будут
# соответствовать правилам задания ключей в словарях.

# def thesaurus(listt):
#     dc = {}
#     for i in listt:
#         dc[i] = [i]
#     print(dc)
#
#
# thesaurus([1, 'www', 'wer', 4, 33])

###################################################################################################################

# 2. Иван решил создать самый большой словарь в мире. Для этого он придумал функцию biggest_dict(**kwargs),
# которая принимает неограниченное количество параметров «ключ: значение» и обновляет созданный им словарь
# my_dict, состоящий всего из одного элемента «first_one» со значением «we can do it». Воссоздайте эту функцию.

# my_dict = {'first_one': 'we can do it'}
#
#
# def biggest_dict(**kwargs):
#     my_dict.update(**kwargs)
#
#
# biggest_dict(www='W', rrr='R', ttt=666, yyy='Y')
# biggest_dict(a1=22, b2=31, c3=11, d4=91)
# print(my_dict)

#############################################################################################################
#
# 3. Дана строка в виде случайной последовательности чисел от 0 до 9. Требуется создать словарь, который
# в качестве ключей будет принимать данные числа (т. е. ключи будут типом int), а в качестве значений – количество
# этих чисел в имеющейся последовательности. Для построения словаря создайте функцию count_it(sequence),
# принимающую строку из цифр. Функция должна возвратить словарь из 3-х самых часто встречаемых чисел.

# some_str = input()
#
#
# def count_it(sequence):
#     first_dict = {int(item): sequence.count(item) for item in sequence}
#     print(first_dict)
#     sorted_first_dict = sorted(first_dict.items(), key=lambda element: element[1])
#     print(sorted_first_dict)
#     return dict(sorted_first_dict[-3:])
#
#
# print(count_it(some_str))


############################################################################################################









