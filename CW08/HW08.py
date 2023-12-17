# ДЗ на пятницу:
# 1. Есть число n - вводится с клавиатуры, выведите первые n чисел последовательности Фибоначчи.

# n = int(input("Введите число: "))
# fib = [0, 1, 1]
# for i in range(3, n):
#     fib.append(fib[i - 2] + fib[i - 1])
# print(f"{n}-первых чисел последовательности Фибоначчи составляют список {fib[:n]}")


# 2. Есть число a - вводится с клавиатуры, вычислите значение факториал a. При а = 5,
# результат = 120. 5 * 4 * 3 * 2 * 1

# a = int(input("Введите число: "))
# f = 1
# for i in range(a, 0, -1):
#     f *= i
# print(f"Факториал числа {a} = {f}")

# 3. Напишите программу, которая проверить является ли число простым,
# то есть делится без остатка только на себя и на единицу.
# Простые числа:
# 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79,
#  83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167,
#  173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257,
#  263, 269, 271, 277, 281, 283, 293)

# a = int(input("Введите число: "))
# count = 0
# for i in range(1, a + 1):
#     if a % i == 0:
#         count += 1
# if count == 2:
#     print(f"Число {a} является простым")
# else:
#     print(f"Число {a} не является простым")

# 1. Напишите сортировку «пузырьком», числа вводятся с клавиатуры

# sp = list(map(int, input("Введите числа через пробел: ").split()))
# for i in range(len(sp) - 1):
#     for j in range(len(sp) - i - 1):
#         if sp[j] > sp[j + 1]:
#             sp[j], sp[j + 1] = sp[j + 1], sp[j]
# print(f"Отсортированный список sp имеет вид - {sp}")

# 2. Пользователь вводит число от 0 до 100, узнайте,
# что за число пользователь ввел, максимум за 7 попыток)
# рекомендую использовать алгоритм бинарного поиска) на каждую из попыток
# программа должна отвечать True/False

p = int(input("Введите число p = "))
count = 0  # счетчик количества шагов
a_min = 0
a_max = 101

while a_min < a_max and count < 7:
    sr = int((a_min + a_max) // 2)
    if p > sr:
        a_min = sr
    elif p < sr:
        a_max = sr
    count += 1
print(sr, count)