# В некой игре-стратегии есть солдаты и герои. У всех есть свойство,
# содержащее уникальный номер объекта, и свойство,
# в котором хранится принадлежность команде. У
# солдат есть метод "иду за героем",
# который в качестве аргумента принимает объект типа "герой".
# У героев есть метод увеличения собственного уровня.
# В основной ветке программы создается по одному герою для каждой команды.
# В цикле генерируются объекты-солдаты. Их принадлежность команде определяется
# случайно. Солдаты разных команд добавляются в разные списки.
# Измеряется длина списков
# солдат противоборствующих команд и выводится на экран.
# У героя, принадлежащего команде с более длинным списком, увеличивается уровень.
# Отправляем одного из солдат следовать за первым героем и выводим их идентификационные номера.

from random import random, randint, sample, choice


class Heroes:

    def __init__(self, id_, teams, level):
        self.id_ = id_
        self.teams = teams
        self.level = level


    def level_up(self, level):
        self.level += 1
        return level

class Solders:

    def __init__(self, id_, teams):
        self.id_ = id_
        self.teams = teams


    def go_from_heroes(self, hero):
        self.hero = hero
        return f"Солдат с номером {Solders.number} следует за героем {Heroes.number}"

heroes_red = Heroes(id_=1, teams="red", level=0)
heroes_blue = Heroes(id_=2, teams="blue", level=0)

solders_red = []
solders_blue = []
n = 0

while n < (randint(1, 7)):
    solder = Solders(id_=(randint(0, 1000)), teams=choice(["red", "blue"]))
    if solder.teams == "red":
        solders_red.append(solder.id_)
    else:
        solders_blue.append(solder.id_)
    n += 1

if len(solders_red) > len(solders_blue):
    heroes_red.level_up(level=1)
    print(solders_red[0])
else:
    heroes_blue.level_up(level=1)
    print(solders_blue[0])


print(solders_red)
print(solders_blue)

print(heroes_red.level)
print(heroes_blue.level)

print(heroes_red.id_)
print(heroes_blue.id_)