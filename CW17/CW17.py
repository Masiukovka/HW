# class Car:
#     def __init__(self, model):
#         self.model = model
#
#
# car1 = Car(model="audi")
# car2 = Car(model="22")
# car3 = Car(model="33")
#
# print(car1)
# print(car2)
# print(car3)

# class Car:
#     _model = "Audi"
#     def __init__(self, model):
#         return f"{Car._model} turn on"
#
#
# print(Car._model)


class Shape:
    color = "red"

class Circle(Shape):
    radius = 5
    color = "blue"

class Rectangle(Shape):
    a = 5
    b = 4

print(Circle.color)
print(Rectangle.color)

a, l = 4, 4
c = a + l
print(float(c))