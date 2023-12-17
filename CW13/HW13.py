# 1. Напишите функцию, которая принимает список вида
# [1, 2, 'aasf', '1', '123', 123, True], и возвращает новый список,
# состоящий только из чисел [1,2,123]
#
# def chislo(lst:list):
#     out = list(filter(lambda x: type(x) == int, lst))
#     return out
#
# lst = [1, 2, 'aasf', '1', '123', 123, True]
#
# print(chislo(lst))

#
# 2. Определите является ли число специальным,
# по определение специальное число - это число,
# которое состоит только из чисел 0, 1, 2, 3, 4 или 5. Например:
# 12 - специальное
# 5 - специальное
# 62 - нет
# 123450 - специальное
# 1234560 - нет

# def spec(num):
#     n = [i for i in str(num)]
#     for i in n:
#         if i not in "012345":
#             return "Нет"
#             break
#         else:
#             return "Специальное"
#
# print(spec(123450))

# 3. Напишите функцию operation_range(start, end, step, operator):
# которая проводит действие, указанное в переменной operator
# над последовательностью от start до end с шагом step. Например:
# operation_range(1, 5, 1, "+") -> 15

from functools import reduce

# def operation_range(start, end, step, operator):
#     num = [i for i in range(start, end + 1, step)]
#     if operator == "+":
#         return reduce(lambda x, y: x + y, num)
#     elif operator == "-":
#         return reduce(lambda x, y: x - y, num)
#     elif operator == "*":
#         return reduce(lambda x, y: x * y, num)
#     elif operator == "/":
#         return reduce(lambda x, y: x / y, num)
#     elif operator == "**":
#         return reduce(lambda x, y: x ** y, num)
#


# print(operation_range(1, 5, 1, "+"))



# 4. Функция принимает число и возвращает сумму квадратов чисел этого чиcла.
# in: 321
# out: 13

# def kv(num):
#     n = [int(i) for i in str(num)]
#     out = sum(list(map(lambda i: i ** 2, n)))
#     return out
#
# num = 321
#
# print(kv(num))
#
# 5. Функция принимает список чисел и сортирует четные от нечентых:
# [5, 8, 6, 3, 4]  =>  [5, 3, 8, 6, 4]

# def sort_ch(lst):
#     chet = list(filter(lambda x: x % 2 == 0, lst))
#     nechet = list(filter(lambda x: x % 2 != 0, lst))
#     return nechet + chet
#
# lst = [5, 8, 6, 3, 4]
#
# print(sort_ch(lst))