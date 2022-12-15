#  Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
n = int(input("Введите число N: "))
result = []
i = 2


while i <= n:
    if n % i == 0:
        if i not in result:
            result.append(i)

        n //= i
    else:
        i += 1
print(result)
