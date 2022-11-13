a = input("Введите последовательность чисел от 0 до 10 через пробел:")
n = int(input("Введите любое число:"))
list_of_strings = a.split()
array = list(map(int, list_of_strings))
print(array)
for i in range(len(array)):
    for j in range(len(array) - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
print(array)


def binary_search(array, low, high, n):
    mid = (high + low) // 2
    if array[mid] == n:
        return mid
    elif n < array[mid]:
        return binary_search(array, low, mid - 1, n)
    elif n > array[mid]:
        return binary_search(array, mid + 1, high, n)
    else:
        return -1


res = binary_search(array, 0, len(array) - 1, n)

if res != -1:
    print("Индекс введёного числа", str(res))
else:
    print("Такого элемента нет в введённой последовательности чисел")

# не получилось задать условие поиска, чтоб искомое число было меньше введенного, но, чтоб следующее было больше или равно введенному.
