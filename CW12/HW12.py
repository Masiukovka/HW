# # 1. Написать функцию, которая принимает строку и возвращает
# # центральный элемент(ы) этой строки.Например:
# # "hasbd" -> "s"
# # "bajshd" -> "js"
#   "hasklbd"


# def sr_symb(t):
#     symb = ""
#     if len(t) % 2 == 0:
#         symb = t[((len(t) // 2) - 1):((len(t) // 2) + 1)]
#     else:
#         symb = t[(len(t) // 2)]
#     return symb
#
# t = "hasklbd"
#
# print(sr_symb(t))

# 2. Написать функцию, принимающую число и возвращающую ближайший к этому числу палиндром.
# 11 -> 22
# 188 -> 191
# 191 -> 202
# 2541 -> 2552
#



# 3. Напишите функцию, которая принимает на вход список строк и возвращает наиболее часто встречающуюся строку.

# def chast(t):
#     out = ""
#     count = 0
#     for i in t:
#         a = i
#         if t.count(a) > count:
#             out = a
#             count = t.count(a)
#     return out
#
#
# t = ["aaa", "vvvv", "aaa", "kjuh", "VVV", "aaa", "jjb", "aaa", "vvvv", "vvvv", "vvvv", "vvvv", "vvvv"]
#
# print(chast(t))

# 4. Напишите функцию, которая принимает на вход два списка и возвращает новый список, содержащий
# элементы, которые есть в обоих списках.

# def poisk(l1, l2):
#     l_out = []
#     for i in l1:
#         if i in l2:
#             l_out.append(i)
#     return l_out
#
# def pov_el(l_1, l_2):
#     out = list(set(poisk(l_1, l_2) + poisk(l_2, l_1)))
#     return out
#
# l_1 = [1, 2, 5, 8, 9]
# l_2 = [3, 0, 9, 8, 7]
#
# print(pov_el(l_1, l_2))


# 5 Напишите функцию, которая принимает на вход строку и возвращает количество слов в этой строке,
# в которых есть более 3-х гласных (a, e, i, o, u, y).

# def count_gl(t):
#     count = 0
#     all_count = 0
#     text = t.split()
#     lst = []
#     for sl in text:
#         for b in sl:
#             if b in "aeiouy":
#                 count += 1
#         if count >= 3:
#             all_count += 1
#
#     return all_count
#
# t = "nkylliyyhviihlil vgygyykoojg mmoocnmvbx kuuhify jcgdsjgcvjh khygyg eegg ruuuoq qwtyuiui"
#
# print(count_gl(t))


# 6. Написать функцию, которая принимает на вход два списка чисел и возвращает новый
# список, содержащий суммы соответствующих элементов этих списков.Списки мб разной длины.Например:
# [1, 2, 3, 4][11, 32] -> [12, 34, 3, 4]

# def sum_lst(l_1, l_2):
#     lst_out = []
#     sum = 0
#     while len(l_1) != len(l_2) or len(l_2) != len(l_1):
#         if len(l_1) > len(l_2):
#             l_2.append(0)
#         else:
#             l_1.append(sum)
#     for i in range(len(l_1)):
#         lst_out.append(l_1[i] + l_2[i])
#     return lst_out
#
# l_1 = [1, 2, 3, 4]
# l_2 = [11, 32]
#
# print(sum_lst(l_1, l_2))

# 7 *.Напишите функцию выведения ряда Фибоначчи, используя рекурсию.

# def fib(num):
#     if num in (1, 2):
#         return 1
#     return fib(num - 1) + fib(num - 2)
#
# print(fib(10))