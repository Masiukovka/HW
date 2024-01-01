# 1. Создайте пользовательскую функцию,
# принимающую произвольное количество именованных аргументов
# и выводящую их затем на экран в формате «key -> value».
# Для вывода элементов полученного словаря используйте цикл for.
# Вызовите функцию, передав ей в качестве значений целое число,
# вещественное число, строку и пустой список.

# def func_return(*args):
#     znach = {"int": char1, "float": char2, "str": char3, "list": char4}
#     for k, v in znach.items():
#         print(f"Ключ {k} значение {v}")
#
# char1=1
# char2=2.3
# char3="hkju"
# char4=["jhk", 5]
# func_return(char1, char2, char3, char4)

# 2. Создайте и вызовите пользовательскую функцию-матрешку my_func_1,
# состоящую из четырех вложенных друг в друга определений аналогичных функций.
# Каждая функция должна выводить сообщение в формате 'In my_func_{номер функции}.',
# а также содержать определение и вызов следующей вложенной функции
# (в последней функции эта часть будет отсутствовать)

# def my_func_01(*args, **kwargs):
#     def my_func_02(*args, **kwargs):
#         def my_func_03(*args, **kwargs):
#             def my_func_04(*args, **kwargs):
#                 def my_func_05(*args, **kwargs):
#                     return print(f"Название функции 5")
#                 my_func_05(*args, **kwargs)
#                 return print(f"Название функции 4")
#             my_func_04(*args, **kwargs)
#             return print(f"Название функции 3")
#         my_func_03(*args, **kwargs)
#         return print(f"Название функции 2")
#     my_func_02(*args, **kwargs)
#     return print(f"Название функции 1")
#
# my_func_01()


# 3. Напишите функцию, рассчитывающую стоимость поездки на такси в зависимости от расстояния.
# В качестве аргументов функция должна принимать именованные параметры:
# км – расстояние поездки в километрах, мин_цена – базовый тариф,
# включающий подачу такси и первые три километра пути,
# цена_за_км – цена за каждый километр, начиная с четвертого.
# Рассчитайте и выведите на экран стоимость поездки за 17.5 км,
# если по умолчанию базовый тариф составляет 2 у.е.,
# а цена за километр сверх минимума – 0.3 у.е.

# def taxi(km, min_cena, cena_za_km):
#     if km > 4:
#         return min_cena + cena_za_km * (km - 3)
#     return min_cena
#
# print(taxi(km=17.5, min_cena=2, cena_za_km=0.3))

# 4.  Напишите функцию, которая будет генерировать случайный пароль.
# В пароле должно быть от 8 до 15 символов Юникода из диапазонов 48-57 (цифры),
# 65-90 (буквы латинского алфавита в верхнем регистре)
# и 97-122 (буквы латинского алфавита в нижнем регистре).
# Сгенерируйте и выведите на экран три пароля.

import random
import string


def parol(*args):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    all_symbol = random.sample(lower + upper + num, length)
    password = "".join(all_symbol)
    return password

length = int(input("Введите количество символов в диапазоне от 8 до 16: "))

print(parol(length))





# 5***. Перед решением этих задач, рекомендую почитать про "замыкание" в ФП.
# https://www.codewars.com/kata/60b775debec5c40055657733
# https://www.codewars.com/kata/5b0a80ce84a30f4762000069


# 1. Создать класс Human c атрибутами name, surname,
# birth_year и двумя методами full_name(),
# который будет  возвращать полное имя: Name Surname и get_age(),
# возвращающий возраст, созданного экземпляра.

# class Human:
#     name = ""
#     surname = ""
#     birth_year = 0
#
#     def full_name(self):
#         return f"{self.name} {self.surname}"
#
#     def get_age(self):
#          return 2024 - self.birth_year
#
# human_1 = Human()
# human_1.name = "Alex"
# human_1.surname = "Kot"
# human_1.birth_year = 1985
# human_2 = Human()
# human_2.name = "Nikita"
# human_2.surname = "Good"
# human_2.birth_year = 2015
# print(f"Фамилия и Имя первого жильца {human_1.full_name()} и его возраст {human_1.get_age()} полных лет.")
# print(f"Фамилия и Имя второго жильца {human_2.full_name()} и его возраст {human_2.get_age()} полных лет.")

# 2. Создайте функцию, Коротая генерирует список, состоящий из словарей,
# с ключам имя и номер телефонах.
# Создайте функцию которая принимает этот словарь и еще один аргумент,
# который мб именем или номером телефона и осуществляет вызов)
# Если соотв. Номера или имени нет в переданном словаре, то вызвать ошибку ValueError
#
#
# def add(contacts):
#     print("Введите имя контакта:")
#     name = input(">")
#     print("Введите номер телефона:")
#     namber = int(input(">"))
#     new_contact = {
#         "name": name,
#         "namber": namber
#     }
#     contacts.append(new_contact)
#
# def search_contact(contacts, search):
#     itog = 0
#     out = ""
#     for contact in contacts:
#         if search == contact["name"]:
#             itog += 1
#             out = contact["name"]
#             break
#         elif search == contact["namber"]:
#             itog += 1
#             out = contact["name"]
#             break
#     if itog == 1:
#         print(f"Происходит набор номера абонента {out}")
#     else:
#         print("ValueError")
#
# search = input("Введите поисковый запрос Имя или номер контакта: ")
#
# contacts = [{"name": "Tom", "namber": "22"}, {"name": "Lev", "namber": "44"}]
#
#
# search_contact(contacts, search)
# print(contacts)
# решены все задачи