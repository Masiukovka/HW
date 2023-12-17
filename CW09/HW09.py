# 1. Напишите функцию, которая принимает список чисел и возвращает список квадратов этих чисел.

# def kv(num):
#     ret_num = []
#     for i in num:
#         ret_num.append(int(i)**2)
#     return ret_num
# num = [2, 5, 3, 6, 1]
# print(kv(num))

# 2. Напишите функцию, которая принимает на вход список строк и возвращает список строк,
# длина которых больше 5 символов.

# def long(s_t):
#     ret_s_t = []
#     for i in s_t:
#         if len(i) > 5:
#             ret_s_t.append(i)
#     return ret_s_t
#
# s_t =["hgjhjy", "hjgjy", "hjh", "jbnvjhbh", "jbv"]
#
# print(long(s_t))

# 3. Напишите функцию, которая принимает на вход список чисел и возвращает
# только четные числа из этого списка.

# def cf(n):
#     ret_n = []
#     for i in n:
#         if i % 2 == 0:
#             ret_n.append(i)
#     return ret_n
#
# n = [2, 5, 3, 6, 1]
#
# print(cf(n))

# 4. Напишите функцию, которая принимает на вход список чисел и возвращает
# сумму квадратов четных чисел из этого списка.

# def sum_kv(n):
#     sum = 0
#     for i in n:
#         if i % 2 == 0:
#             sum += i ** 2
#     return sum
#
# n = [2, 5, 3, 6, 1]
#
# print(sum_kv(n))

# 5. Напишите функцию, которая принимает на вход список строк и возвращает
# список строк, которые начинаются с буквы "a".

# def first_a(t):
#     ret_a = []
#     for i in t:
#         for j in i:
#             if j[0] == "a":
#                 ret_a.append(i)
#     return ret_a
#
# t =["agjhjy", "hjgjy", "ajh", "jbnvjhbh", "abv"]
#
# print(first_a(t))

# 6. Напишите функцию, которая принимает на вход список чисел и возвращает
# список чисел, которые больше 10 и меньше 20.

# def b_m(n):
#     ret_b_m = []
#     for i in n:
#         if 10 < i < 20:
#             ret_b_m.append(i)
#     return ret_b_m
#
# n = [2, 11, 10, 20, 19, 36]
#
# print(b_m(n))

# 7. Напишите функцию, которая принимает на вход список строк и возвращает
# список строк, которые содержат букву "e".

# def b_e(t):
#     ret_e = []
#     for i in t:
#         if i.find("e") >= 0:
#             ret_e.append(i)
#     return ret_e
#
# t =["agjhjy", "hjgey", "aje", "jbnvehbh", "abv"]
#
# print(b_e(t))

# 8. Напишите функцию, которая принимает на вход список чисел и возвращает True,
# если все числа в списке положительные, и False в противном случае.

# def t_f(n):      # переделать слишком долгий код
#     count = 0
#     for i in n:
#         if i >= 0:
#             count += 1
#     if count == len(n):
#         return True
#     else:
#         return False
#
# n = [2, 11, -1, 20, 0, 36]
#
# print(t_f(n))

# 9. Напишите функцию, которая принимает на вход список строк и возвращает список строк,
# которые содержат только цифры.

def t_c(t):
    ret_c = []
    for i in t:
        if i.isdigit():
            ret_c.append(i)
    return ret_c

t =["agjhjy", "222", "a1e", "jbnvehbh", "a61"]

print(t_c(t))
