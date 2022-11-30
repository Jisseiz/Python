# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
from math import factorial

n = int(input('Введите число N: '))
def f(x): return ((x == 1) and 1) or x * factorial(x - 1)


list2 = list(f(i) for i in range(1, n + 1))
print(list2)
