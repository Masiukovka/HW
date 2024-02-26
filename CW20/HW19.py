# ДЗ: Есть class Human, характеристиками которого являются:
# Имя
# Возраст
# Наличие денег
# Наличие собственного жилья

# Человек может:
# Предоставить информацию о себе
# Заработать деньги
# Купить дом.

# Также же есть class Дом, к свойствам которого относятся:
# Площадь
# Стоимость

# Для Дома можно:
# Применить скидку на покупку

# Задание: Реализовать описанную структуру и проверить методы предоставления скидки и
# приобретения дома. Сгенерировать несколько экземпляров класса Дом и Human. Далее
# написать функцию, которая подберет наилучший дом для человека, на основании площади
# и кол-ва денег у него на счету, а так же выведет список домов, которые можно
# рекомендовать. Параметры для рекомендации можно выбрать любые.Например, если
# применить скидку стоимость дома будет подходящей, если человек заработает еще, стоимость
# так же будет подходящей.

class Human:

    def __init__(self, name, age, money, my_home):
        self.name = name
        self.age = age
        self.money = money
        self.my_home = my_home

    def visit_card(self):
        return f"Меня зовут {self.name} и мне {self.age} года"

    def salary_year(self, salary_month):
        return (12 * salary_month)

    def buy_house(self, cost_home):
        return


class Home:
    def __init__(self, square, cost):
        self.square = square
        self.cost = cost

    def discont(self, percent):
        return (self.cost * (percent/100))
list_human = []
human_01 = Human("Antony", 25, 10000, "Yes")
list_human.append(human_01)
human_02 = Human("Tomy", 32, 100000, "No")
list_human.append(human_02)
human_03 = Human("Anna", 22, 5000, "No")
list_human.append(human_03)
list_home = []
home_01 = Home(200, 1000000)
list_home.append(home_01)
home_02 = Home(100, 200000)
list_home.append(home_02)
home_03 = Home(75, 150000)
list_home.append(home_03)
print(list_human)
print(list_home)