# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

a1 = int(input('Введите Ax координат: '))
a2 = int(input('Введите Ay координат: '))
b1 = int(input('Введите Bx координат: '))
b2 = int(input('Введите By координат: '))

result = round(((b1 - a1) ** 2 + (b2 - a2) ** 2) ** (0.5), 3)
print(f'Длинна отрезка: ', result)
