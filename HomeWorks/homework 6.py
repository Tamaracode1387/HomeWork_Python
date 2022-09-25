# Предложить улучшения кода для уже решённых задач:
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

########################################################################################################

# 1. Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве 
# символа-разделителя используйте пробел.

# some_str = input()
# print(max(list(map(int, some_str.split()))), min(list(map(int, some_str.split()))))


#########################################################################################################


# 2. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

# my_list = [1, 1, 2, 3, 4, 4, 5]
# print(tuple(filter(lambda num: my_list.count(num) == 1, my_list)))

###########################################################################################################


# 3. Дана последовательность чисел. Нужно выбрать четные и составить список пар (число; квадрат числа)

# def select(f, col):
#     return [f(x) for x in col]

# def where (f, col):
#     return [x for x in col if f(x)]

# data = '1 2 3 4 5 6 7'.split()

# result = select(int, data)
# result = where(lambda x: not x % 2, result)
# result = select(lambda x: (x, x**2), result)
# print(result)

###########################################################################################################

# 4. Найти сумму чисел списка стоящих на нечетной позиции

# my_list = [1, 1, 2, 3, 4, 4, 5]
# print(my_list)
# sum_list = sum(my_list[item] for item in range(1, len(my_list), 2))
# print(f'Cумма чисел, стоящих на нечётных позициях равна {sum_list}.')


























# 1. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.

# import Func_list_generation as lg
# numbers_list = lg.list_generation()
# result_list = list(filter(lambda a: numbers_list.count(a) == 1, numbers_list))
# print(f'Для последовательности {numbers_list}, \n   список уникальных элементов => {result_list}')



# # 2. Найти сумму чисел списка стоящих на нечетной позиции/

# import Func_list_generation as lg
# numbers_list = lg.list_generation()
# sum_odd = sum(numbers_list[item] for item in range(1, len(numbers_list), 2))
# odd_el = str([numbers_list[item] for item in range(1, len(numbers_list), 2)]).strip('[]')
# print(f'Для списка {numbers_list} сумма чисел, стоящих на нечётных позициях: \n{odd_el} равна {sum_odd}.')



# # 3. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.

# f = '3*x+1'
# n = int(input('Количество элементов словаря: '))
# d = {x: eval(f) for x in range(1, n+1)}
# print(f'для {n = }: {d}')