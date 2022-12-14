# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.

# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# numbers = []
# for _ in range(5):
#     n = int(input('Введите число: '))
#     numbers.append(n)
# print(numbers)
# sum = 0
# for i in range(len(numbers)):
#     if i % 2 != 0:
#         sum += numbers[i]
# print(sum)

###############################################################################################################################

# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# numbers = []
# for _ in range(int(input('Введите кол-во элементов: '))):
#     n = int(input('Введите число: '))
#     numbers.append(n)
# print(numbers)

# a = []
# if len(numbers) % 2 != 0:
#     for i in range(int(len(numbers)/2+1)):
#         a.append(numbers[i]*numbers[len(numbers)-1-i])
#     print(a)
# else:
#     for i in range(int(len(numbers)/2)):
#         a.append(numbers[i]*numbers[len(numbers)-1-i])
#     print(a)
   

############################################################################################################################

# 3. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и 
# минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# a = [1.1, 1.2, 3.1, 5, 10.01]
# print(a)
# b = []
# for i in a:
#     if i % 1 !=0:
#         b.append(round(i % 1, 2))
# print(b)
# print(max(b)-min(b))

############################################################################################################################

# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# number = int(input('Введите десятичное число: '))
# result = ""
# while number != 0:
#     result = str(number%2) + result
#     number //= 2
# print(result)



###########################################################################################################################

# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

# n = int(input())
# fib_list = [0]*(n*2+1)
# print(fib_list)
# fib_list[n] = 0
# fib_list[n+1] = 1
# for i in range(n+2, len(fib_list)):
#     fib_list[i] = fib_list[i-2] + fib_list[i-1]
# for i in range(n, -1, -1):
#     fib_list[i] = fib_list[i+2]-fib_list[i+1]
# print(fib_list)





