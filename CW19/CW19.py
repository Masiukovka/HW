# Создать класс Robot
# Класс инициализируется начальными координатами – положением Робота на
# плоскости, обе координаты заключены в пределах от 0 до 100.
# Робот может передвигаться на одну клетку вверх (N), вниз (S), вправо (E), влево (W).
# Выйти за границы плоскости Робот не может.
# Метод move() принимает строку – последовательность команд перемещения робота,
# каждая буква строки соответствует перемещению на единичный интервал в направлении,
# указанном буквой. Метод возвращает список координат – конечное положение Робота
# после перемещения


class Robot:

    def __init__(self, x: int, y: int):
        if (x < 0 or x > 100) or (y < 0 or y > 100):
            raise Exception
        self.x = x
        self.y = y

    def move(self, movement: str):
        for s in movement:
            match s:
                case "N":
                    self.y += 1
                    if self.y > 100:
                        return self.y - 1, self.x
                case "S":
                    self.y += 1
                    if self.y < 0:
                        return self.y + 1, self.x
                case "E":
                    self.x += 1
                    if self.x > 100:
                        return self.x - 1, self.y
                case "W":
                    self.x += 1
                    if self.x < 0:
                        return self.x + 1, self.y
        return self.x, self.y


robot_1 = Robot(100, 100)
print(robot_1.move("NNNNNNNNNWWWWWEEEEEEEE"))

# Написать декоратор по замеру времени и сравнение работы цикла While и if

