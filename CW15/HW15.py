# 2. Напишите декоратор, замеряет время выполнения функции и кол-во памяти, которое занимает ответ.
#import datetime
import time


def timer_func(pokupki):
    def wrapped(*args, **kwargs):
        start_time = time.perf_counter()
        pokupki(*args, **kwargs)
        end_time = time.perf_counter()
        print(f"Время выполнения функции заняло {end_time - start_time:0.6f} сек.")
    return wrapped
#
# @timer_func
# def pokupki(dengi: str, korzina_pokupok: list)-> dict:
#     dengi = int(dengi)
#     count = 0
#     out = {"status": "", "comment": ""}
#     for tovar in korzina_pokupok:
#         count += tovar.get("count") * tovar.get("price")
#     if count <= int(dengi):
#         out = {"status": "success", "comment": "Покупки оплачены. Ваша сдача " + str(dengi - count) + " рублей"}
#     else:
#         out = {"status": "fail", "comment": "Недостаточно средств. Внесите " + str(count - dengi) + " рублей"}
#     return print(out)
#
# dengi = "100"
# korzina_pokupok = [
#     {"name": "молоко", "count": 2, "price": 3},
#     {"name": "сметана", "count": 3, "price": 4},
#     {"name": "батон", "count": 1, "price": 2},
#     {"name": "шоколадка", "count": 2, "price": 6},
#     ]
# pokupki(dengi, korzina_pokupok)

# 1. На входе программа получает список целых чисел s.
# Ваша задача - вывести следующие списки по одному в строке:
# Список, состоящий из квадратов s.

# @timer_func
# def kvadrat_chisel(spisok_chisel: list)->list:
#     return [num ** 2 for num in spisok_chisel]
#
# # Список, состоящий из остатков деления на 11 элементов s.
# def ostatok_delenia_11(spisok_chisel: list)->list:
#     return [num % 11 for num in spisok_chisel]
#
# # Список, состоящий только из чётных элементов s.
# def spisok_chetnyh(spisok_chisel: list)->list:
#     return [num for num in spisok_chisel if num % 2 == 0]
#
# # Список, состоящий только из элементов s с нечётным количеством цифр.
# def spisok_count_nechet(spisok_chesel: list)->list:
#     return [num for num in spisok_chesel if len(str(num)) % 2 == 1]
#
# # Список, состоящий только из двухзначных элементов s, записанных 2 раза подряд.
# def two_ryadom(spisok_chisel: list)->list:
#     # spisok_dvyznach = list(num for num in spisok_chisel if len(str(num)) == 2)
#     # sosedi_ravny = []
#     #
#     # for i in range(len(spisok_chisel)):
#     #     if spisok_chisel[i - 1] == spisok_chisel[i]:
#     #         sosedi_ravny.append(spisok_dvyznach[i - 1])
#     #         sosedi_ravny.append(spisok_dvyznach[i])
#     # return sosedi_ravny
#     spisok_dvyznach = list(num for num in spisok_chisel if len(str(num)) == 2)
#     sosedi_ravny = []
#     #
#     for i in range(len(spisok_dvyznach)):
#         if spisok_dvyznach[i - 1] == spisok_dvyznach[i]:
#             sosedi_ravny.append(spisok_dvyznach[i - 1])
#             sosedi_ravny.append(spisok_dvyznach[i])
#     return sosedi_ravny
#
# # Список, состоящий из элементов s, стоящих на позициях, не кратных 3. позиция 0 кратна 3?
#
def pos_ne_kr_3(spisok_chisel):
# #1
    lst = []
#     # lst.append(spisok_chisel[0])
#     # lst.extend(list(spisok_chisel[i] for i in range(len(spisok_chisel)) if i % 3 != 0))
#     # return lst
#     #return [spisok_chisel[i] for i in range(len(spisok_chisel)) if i % 3 != 0]
# #2
#     return [spisok_chisel[i] for i in range(len(spisok_chisel)) if len(spisok_chisel[i]) == 2 and i % 3 != 0]
#3
    del spisok_chisel[::3]
    return spisok_chisel

#
spisok_chisel = [22, 22, 45, 60, 122, 225, 66, 66, 369, 1000, 1245]
# #               [0    1   2   3    4   5    6   7   8     9     10]
#
# print(kvadrat_chisel(spisok_chisel))
# print(ostatok_delenia_11(spisok_chisel))
# print(spisok_chetnyh(spisok_chisel))
# print(spisok_count_nechet(spisok_chisel))
# print(two_ryadom(spisok_chisel))
print(pos_ne_kr_3(spisok_chisel))


# 3. Напишите декоратор, который будет корректировать результат функции,
# а именно помещать их в словарь. {"status": "success", "result": ...}

# def timer_func(pokupki):
#     def wrapped(*args, **kwargs):
#         start_time = time.perf_counter()
#         pokupki(*args, **kwargs)
#         end_time = time.perf_counter()
#         print(f"Время выполнения функции заняло {end_time - start_time:0.6f} сек.")
#     return wrapped


# def korrekt_korzin(pokupki):
#     def wrapped(*args, **kwargs):
#         ball = 0
#         count = 0
#         for tovar in korzina_pokupok:
#             count += tovar.get("count") * tovar.get("price")
#         if count >= 100:
#             ball = 10
#         return pokupki(ball, *args, **kwargs)
#     return wrapped
#
#
# #@timer_func
# @korrekt_korzin
# def pokupki(ball: int, dengi: str, korzina_pokupok: list)-> dict:
#     dengi = int(dengi)
#     count = 0
#     # ball = 0
#     out = {"status": "", "comment": "", "ball": ""}
#     for tovar in korzina_pokupok:
#         count += tovar.get("count") * tovar.get("price")
#     if count <= int(dengi):
#         out = {"status": "success",
#                "comment": "Покупки оплачены. Ваша сдача " + str(dengi - count) + " рублей",
#                "ball": "Начисленно " + str(ball) + " баллов"}
#     else:
#         out = {"status": "fail",
#                "comment": "Недостаточно средств. Внесите " + str(count - dengi) + " рублей",
#                "ball": "Начисленно " + str(ball) + " баллов"}
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

