# Источник для будущего: https://webdevblog.ru/# nasledovanie-i-kompoziciya-rukovodstvo-po-oop-python/?ysclid=lr4qs3jvos553770059
# 1. Построить иерархию классов, удовлетворяющую следующим условиям
# (тематика иерархии на ваше усмотрение):
# - Количество классов >= 5.
# - Использовать наследование, в т.ч. множественное
# - Для каждого класса определить минимум 3 магических метода (на ваш выбор)
# - Создать экземпляры для каждого класса
# -  Иерархия должна быть логичной и не противоречить принципам ООП.
# Обработка ЗП - т.к. пригодится

"""Programm"""
class Zarplatnaya_vedomost:
    def svodnaya_vedomost(self, employees):
        nazvanie_tabl = "Сводная ведомость начисленной заработной платы"
        print(nazvanie_tabl)
        print("*" * len(nazvanie_tabl))
        for employee in employees:
            print(f"Начисление для сотрудника с табельным № {employee.id} "
                  f"Подразделение {employee.otdel} "
                  f"ФИО {employee.full_name}")
            print(f"Начисленная сумма {employee.svodnaya_vedomost()}")
            print("#" * len(nazvanie_tabl))


class Employee:
    def __init__(self, id, otdel, full_name):
        self.id = id
        self.otdel = otdel
        self.full_name = full_name



class MonthEmployee(Employee):
    def __init__(self, id, otdel, full_name, baze_chast, premiya):
        super().__init__(id, otdel, full_name)
        self.baze_chast = baze_chast
        self.premiya = premiya

    def svodnaya_vedomost(self):
        return self.baze_chast + (self.baze_chast * self.premiya)


class HourEmployee(Employee):
    def __init__(self, id, otdel, full_name, hours_worked, hour_pay):
        super().__init__(id, otdel, full_name)
        self.hours_worked = hours_worked
        self.hour_pay = hour_pay

    def svodnaya_vedomost(self):
        return self.hours_worked * self.hour_pay

class PodryadEmployee(Employee):
    def __init__(self, id, otdel, full_name, fix_pay):
        super().__init__(id, otdel, full_name)
        self.fix_pay = fix_pay

    def svodnaya_vedomost(self):
        return self.fix_pay

