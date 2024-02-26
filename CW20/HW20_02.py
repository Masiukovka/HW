# 1. Создать класс, который в кач-ве аргументов принимает переменные a, b, g.
# 2. С помощью маг.метода new переопределить названия этих переменных
# как alpha, betta, gamma, соответственно.
# 3. Почитать про метакласс type()
# 4. Почитать про виды исключений в python.
# Блок try/except/finally/else и создание своих классов исключений.

class Peremen:

    def __new__(cls, a, b, g):
        return super().__new__(cls)

    def __init__(self, alpha, betta, gamma):
        self.a = alpha
        self.b = betta
        self.g = gamma

    def znach(self):
        return self.alpha * self.betta * self.gamma

zn = Peremen.znach(3, 2, 10)
print(zn)