# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
import sys

x = int(input('Введите X координат: '))
y = int(input('Введите Y координат: '))


if x > 0 and y > 0:
    quarterNumber = 1
elif x < 0 and y > 0:
    quarterNumber = 2
elif x < 0 and y < 0:
    quarterNumber = 3
elif x == 0 or y == 0:
    sys.exit('Координата не должна быть равна 0')
else:
    quarterNumber = 4
print(f"Точка находится в {quarterNumber} четверти плоскости")
