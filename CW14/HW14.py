# 1. Реализуйте декоратор, который проверяет аргументы функции на тип данных. Соответствие
# аннотациям. Рекомендую использовать метод annotations.В качестве результата возвращаем значение bool.

# def type_vvoda(schet):
#     def decorator(num):
#         if type(num) is schet.__annotations__:
#             print(f'Type значения {num} в аннотации указан верно')
#             schet(num)
#         else:
#             print(f"Type значения {num} указан неверно")
#             schet(num)
#     return decorator

def type_vvoda(schet):
    def wrapper(*args, **kwargs):
        annotations = schet.__annotations__
        for name, val in kwargs.items():
            if name in annotations and not isinstance(val, annotations(name)):
                raise "error"
        print(schet(*args, **kwargs))
    return wrapper

@type_vvoda
def schet(num: str)->int:
    return f"{num} iuhjyg"


schet(num=5)


# попробовал привязать ко 2-й задаче, но что-то пошло не так))
# def type_vvoda(vvod_login):
#     def annot(login, spisok_to_dostup):
#         for arg1, arg2 in vvod_login.annotations:
#             if type(arg1) == vvod_login.annotations and type(arg2) == vvod_login.annotations:
#                 print(f'Type {login} and {spisok_to_dostup} указаны верно')
#             else:
#                 print("Тип данных одного из параметров указан неверно")
#         return annot
#     return type_vvoda


# 2. Создайте декоратор, который ограничивает доступ к функции определенным типам пользователей.
# Предполагается, что # тип пользователя будет передаваться в качестве аргумента user_type(str)
# в декорируемую функцию.
# Типы пользователей: "admin", "user", "auth_user". Результат должен быть вида: "access",
# если разрешен "denied", если нет.

# def proverca_dostupa(vvod_login):
#     def wrapper(login, spisok_to_dostup):
#         print("Проверка доступа к выполгнению функции у пользователя:", login)
#         if login in spisok_to_dostup:
#             print(f"Доступ пользователю {login} разрешен")
#             vvod_login(login, spisok_to_dostup)
#         else:
#             print(f"Доступ пользователю {login} запрещен")
#     return wrapper
#
# #@type_vvoda
# @proverca_dostupa
# def vvod_login(login: str, spisok_to_dostup: list):
#     print("Ура сработало!!! Я почти admin))))")
#
# spisok_to_dostup = ["admin", "user", "auth_user"]
# login = 222
# vvod_login(login, spisok_to_dostup)

# 3. Напишите функцию, которая принимает два аргумента: кол - во денег в наличии(str) и корзина
# покупателя(list[dict]). Далее проверяет хватает ли денег на оплату всех товаров из корзины.
# В случае, если хватает возвращает ответ вида: {
#     "status": "success",
#     "comment": "Покупки оплачены"
# }
# Если денег не хватает ответ должен быть: {
#     "status": "fail",
#     "comment": "Недостаточно средств. Внесите n сумму денег"
# }
# n - количество денег, которое не хватает для оплаты всех товаров корзина представляет собой
# список словарей с ключами: название, количество, стоимость.

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
#
# dengi = "100"
# korzina_pokupok = [
#     {"name": "молоко", "count": 2, "price": 3},
#     {"name": "сметана", "count": 3, "price": 4},
#     {"name": "батон", "count": 1, "price": 2},
#     {"name": "шоколадка", "count": 2, "price": 6},
#     ]
# pokupki(dengi, korzina_pokupok)