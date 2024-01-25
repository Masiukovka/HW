# # numbers = "8 3 -5 42 -1 0 0 -9 4 7 4 -4"
# # out = sorted([int(x) for x in numbers.split(" ")], reverse=True)
# # print(out[0], out[-1])
# #
# # url = "www.codewars.com/katas/?page=1#about"
# #
# # print(url.split('#')[0])
#
# # Домашнее задание:
# # 1. Построить иерархию классов, удовлетворяющую следующим условиям
# # (тематика иерархии на ваше усмотрение):
# # - Количество классов >= 5.
# # - Использовать наследование, в т.ч. множественное
# # - Для каждого класса определить минимум 3 магических метода (на ваш выбор)
# # - Создать экземпляры для каждого класса
# # -  Иерархия должна быть логичной и не противоречить принципам ООП.
#
# # 2. Дополнительно почитать про принципы ООП, SOLID, DRY, KISS.
#
# # 3. Почитать про MRO (Diamond problem)
#
# class Figure:
#     def __init__(self, color):
#         self.color = color
#
#     def __str__(self):
#         return f"Figure {self.color}"
#
#     def __repr__(self):
#         return f"Squere {self.color}"
#
# class Squere(Figure):
#     def __init__(self, side, color):
#         super().__init__(side, color)
#         self.side = side
#         self.color = color
#
#     def __str__(self):
#         return f"Squere {self.color}"
#
#     def __repr__(self):
#         return f"Squere {self.color}"
#
#
# class Circul(Figure):
#     def __init__(self, side, color):
#         super().__init__(side, color)
#         self.side = side
#         self.color = color
#
#     def __str__(self):
#         return f"Squere {self.color}"
#
#     def __repr__(self):
#         return f"Squere {self.color}"


def to_jaden_case(string):
    t = string.split(" ")
    return " ".join([i[0].capitalize() + i[1:].lower() for i in t])

string = "How can mirrors be real if our eyes aren't real"
print(to_jaden_case(string))


