import math

def square(side):

    area = side * side
    if not isinstance(side, int):
        area = math.ceil(area)
    return area

side_input = input("Введите размер стороны квадрата: ")

try:

    side_value = float(side_input)

    if side_value.is_integer():
       side_value = int(side_value)

    result = square(side_value)
    print(f"Площадь квадрата со стороной {side_value} равна: {result}")
except ValueError:
    print("Ошибка! Пожалуйста, введите число.")

