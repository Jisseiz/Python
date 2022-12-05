# Напишите программу, которая найдёт произведение пар чисел списка.
import math

arr = [2, 3, 4, 5, 6]
result = []
lenght = math.floor(len(arr)/2)
i = 0


while i < lenght:
    result.append(arr[i] * arr[-i-1])
    i += 1
if len(arr) % 2 != 0:
    result.append(arr[lenght] * arr[-lenght-1])
print(result)
