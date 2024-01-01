# 1. Создайте пользовательскую функцию,
# принимающую произвольное количество именованных аргументов
# и выводящую их затем на экран в формате «key -> value».
# Для вывода элементов полученного словаря используйте цикл for.
# Вызовите функцию, передав ей в качестве значений целое число,
# вещественное число, строку и пустой список.

# def func_return(char1=int, char2=float, char3=str, char4=list) -> dict:
#     znach = {"int": char1, "float": char2, "str": char3, "list": char4}
#     return znach
#
#
# zn_dict = func_return(char1=1, char2=2.3, char3="hkju", char4=["jhk", 5])
# for k, v in zn_dict.items():
#     print(f"Ключ {k} значение {v}")