import Zarabotnaya_plata

monthEmployee = Zarabotnaya_plata.MonthEmployee(121, "Конструктор",
                                                "Костя Иванов", 1200, 0.4)
hourEmployee = Zarabotnaya_plata.HourEmployee(323, "Слесарь",
                                              "Иван Петров", 25, 30)
podryadEmployee = Zarabotnaya_plata.PodryadEmployee(555, "Торговый представитель",
                                                    "Ольга Вторая", 1000)
zarplatnaya_vedomost = Zarabotnaya_plata.Zarplatnaya_vedomost()
zarplatnaya_vedomost.svodnaya_vedomost([monthEmployee,
                                        hourEmployee,
                                        podryadEmployee])
