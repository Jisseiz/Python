# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
from random import randint
import itertools

k = randint(2, 7)


def ratios(k):
    ratios = [randint(0, 10) for i in range(k + 1)]
    while ratios[0] == 0:
        ratios[0] = randint(1, 10)
    return ratios


def polynomial(k, ratios):
    var = ['*x^']*(k-1) + ['*x']
    polynomial = [[a, b, c] for a, b, c in itertools.zip_longest(
        ratios, var, range(k, 1, -1), fillvalue='') if a != 0]
    for x in polynomial:
        x.append(' + ')
    polynomial = list(itertools.chain(*polynomial))
    polynomial[-1] = ' = 0'
    return "".join(map(str, polynomial)).replace(' 1*x', ' x')


ratios = ratios(k)
polynom1 = polynomial(k, ratios)
print(polynom1)

with open('less4.txt', 'w') as data:
    data.write(polynom1)
