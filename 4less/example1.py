# Вычислить число Пи c заданной точностью d
import math

d = input('Введите D: ')
count = len(d)
pi = str(math.pi)
print(pi[:count])
