# def summ(x):
#     def summ_2(y):
#         return x * y
#     return summ_2
#
# summs = []
# for x in range(1, 5):
#     summs.append(summ(x))
#
# s_1, s_2, s_3, s_4 = summs
#
# print(s_1(10))
# print(s_2(10))
# print(s_3(10))
# print(s_4(10))
#
# def say():
#     slovo = "Привет"
#     print(hex(id(slovo)))
#     def repeet():
#         print(hex(id(slovo)))
#         print(slovo)
#     return repeet
#
# func = say()
# print(func.__code__.co_freevars)
# print(func.__closure__)
#
#
# def two_sum(numbers, target):
#     out = []
#     for i in range(len(numbers)):
#         for j in range(i + 1, len(numbers)):
#             if numbers[i] + numbers[j] == target:
#                 out.append(i)
#                 out.append(j)
#     return tuple(out)
#
# numbers = [1 ,2, 3]
# target = 4
# print(two_sum(numbers, target))

https://www.codewars.com/kata/5714eb80e1bf814e53000c06/python
import operator
import functools


def fish_hex(name):
    out = [t for t in name if t.lower() in "abcdef"]
    if len(out) == 0:
        return 0
    else:
        numbers = [int((t), 16) for t in out]
    # result = reduce(lambda x, y: map(xor, x, y), numbers)
    # fish is 15
    return functools.reduce(operator.xor, numbers)

name = 'E uXxZI zjXDlMgBs'

print(fish_hex(name))