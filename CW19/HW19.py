# 1. Создать класс Snow. Класс содержит целое число - количество снежинок.
# Класс включает методы перегрузки арифметических операторов сложения, вычитания,
# умножения и деления. Код этих методов должен выполнять увеличение
# или уменьшение количества снежинок на число n или в n раз.
# Класс также включает метод makeSnow(), который принимает сам объект и число
# снежинок в ряду, а возвращает строку вида
# "*****\n*****\n*****…",  где количество снежинок между '\n' равно переданному аргументу,
# а количество рядов вычисляется, исходя из общего количества снежинок.

class Snow:
    all_snow = 5
    object_snow = "*"

    def __init__(self, operant_snow, n): # исключил переменную
        self.operant_snow = operant_snow
        self.n = n


    def umnozhenie(n):
        return Snow.all_snow * n

    def delenie(n):
        return round(Snow.all_snow / n)

    def slozhenie(n):
        return round(Snow.all_snow + n)

    def vychitanie(n):
        return round(Snow.all_snow - n)

    def makeSnow(operant_snow, n):
        if operant_snow == "*":
            str_snow = Snow.umnozhenie(n) * Snow.object_snow
        elif operant_snow == "/":
            str_snow = Snow.delenie(n) * Snow.object_snow
        elif operant_snow == "+":
            str_snow = Snow.slozhenie(n) * Snow.object_snow
        elif operant_snow == "-":
            str_snow = Snow.vychitanie(n) * Snow.object_snow
        out_snow = "\\n".join(str_snow[0:n] for t in range(0, len(str_snow), n))
        return out_snow

    # def __str__(self):
    #     return Snow.out_str

    def __repr__(self):
        return Snow.out_str



snezhok_um = Snow.makeSnow("*", 3)
snezhok_delenie = Snow.makeSnow("/", 1)
snezhok_slozhenie = Snow.makeSnow("+", 3)
snezhok_vychital = Snow.makeSnow("-", 1)


print(snezhok_um)
print(snezhok_delenie)
print(snezhok_slozhenie)
print(snezhok_vychital)
