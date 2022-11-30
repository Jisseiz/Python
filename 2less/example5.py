# Реализуйте алгоритм перемешивания списка.
arr = [1, 2, 3, 4, 5, 6]


for i in arr:
    [arr[i], arr[i+1]] = [arr[i+1], arr[i]]
print(arr)
