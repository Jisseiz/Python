# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.(для продвинутых - с файлом, вариант минимум - ввести позиции в консоли)
def collection(n):
    arr = []
    for i in range(-n, n+1):
        arr.append(i)
    print(arr)
    mult = arr[0]*arr[1]
    print(mult)


x = int(input("Введите число N: "))
collection(x)
