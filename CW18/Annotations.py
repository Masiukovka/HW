from typing import NamedTuple

class EmployeeAnnotation(NamedTuple):
    id: int
    otdel: str
    full_name: str

class MonthEmployeeAnnotation(NamedTuple):
    baze_chast: float
    premiya: float

    def svodnaya_vedomost_Annotation(self):
        """Returns the full amount of accrued wages"""
class HourEmployeeAnnotation(NamedTuple):
    hours_worked: float
    hour_pay: float

    def svodnaya_vedomost_Annotation(self):
        """Returns accrued wages for hours worked"""

class PodryadEmployeeAnnotation(NamedTuple):
    fix_pay: int

    def svodnaya_vedomost_Annotation(self):
        """Returns the amount specified in the contract"""
        
