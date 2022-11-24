# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. ¬ - Отрицание ⋁ - логическое "Или" ⋀ - логическое "И"
x = int(input('Введите X: '))
y = int(input('Введите Y: '))
z = int(input('Введите Z: '))


left = not (x or y or z)
right = not x and not y and not z
result = left == right
print(result)
