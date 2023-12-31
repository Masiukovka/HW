# Задачи на декораторы:
# 1. Напишите декоратор, оптимизирующий работу декорируемой функции.
# Декоратор должен сохранять результат работы функции на ближайшие три запуска
# и вместо выполнения функции возвращать сохранённый результат.
# После трёх запусков функция должна вызываться вновь, а результат работы функции — вновь кешироваться.

from time import sleep


def counter(func):
    rez = func("gjg")
    count = 0
    def wrapper(*args):
        nonlocal count
        nonlocal rez
        count += 1
        if count <= 3:
            return rez
        else:
            count = 1
            rez = func(*args)
            return rez
    return wrapper

@counter
def difF(word):
    sleep(3)
    return f"{word}"



print(difF("hgjyg"))
print(difF("gjhj"))
print(difF("HKG"))
print(difF("HKG"))
print(difF("HKG"))

# 2. Напишите декоратор, который будет считать кол-во вызовов функции в файле.

# def counter(func):
#     def wrapper(*args, **kwargs):
#         wrapper.counter += 1
#         print(f"Вызов функции {wrapper.counter}")
#         return func(*args, **kwargs)
#     wrapper.counter = 0
#     return wrapper
#
# @counter
# def pokupki(dengi: str, korzina_pokupok: list)-> dict:
#     dengi = int(dengi)
#     count = 0
#     for tovar in korzina_pokupok:
#         count += tovar.get("count") * tovar.get("price")
#     if count <= int(dengi):
#         out = {"status": "success",
#                "comment": "Покупки оплачены. Ваша сдача " + str(dengi - count) + " рублей"}
#     else:
#         out = {"status": "fail",
#                "comment": "Недостаточно средств. Внесите " + str(count - dengi) + " рублей"}
#     return out
#
# dengi = "100"
# korzina_pokupok = [
#     {"name": "молоко", "count": 2, "price": 50},
#     {"name": "сметана", "count": 3, "price": 4},
#     {"name": "батон", "count": 1, "price": 2},
#     {"name": "шоколадка", "count": 2, "price": 6},
#     ]
# print(pokupki(dengi, korzina_pokupok))
# print(pokupki(dengi, korzina_pokupok))
# print(pokupki(dengi, korzina_pokupok))


# 3. Напишите декоратор, который будет возвращать текст: "Сервер перегружен.
# Повторите попытку позже", если декорируемая функция выполняется более 3-х секунд.

# import time
#
# def timer_func(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.perf_counter()
#         func(*args, **kwargs)
#         end_time = time.perf_counter()
#         if (end_time - start_time) < 3:
#             return print(f"Время выполнения функции подсчета квадратов чисел "
#                          f"с результатом равным: {func(*args, **kwargs)} заняло {end_time - start_time:0.6f} сек."
#                          f"Что меньше допустимого ограничения в 3 сек. Функция выполнена.")
#         else:
#             return print("Сервер перегружен. Повторите попытку позже")
#     return wrapper
#
# def rez(func):
#     def wrapper(*args, **kwargs):
#         print(func(*args, **kwargs))
#         return func(*args, **kwargs)
#     return wrapper
#
# @timer_func
# @rez
# def kvadrat_chisel(spisok_chisel: list)->list:
#     return [num ** 2 for num in spisok_chisel]
#
# spisok_chisel = [22, 22, 45, 60, 122, 225, 66, 66, 369, 1000, 1245]
#
# kvadrat_chisel(spisok_chisel)
