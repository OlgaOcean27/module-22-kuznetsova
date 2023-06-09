array = list(map(int, input('Введите числа через пробел: ').split()))
print(array)

low = 0
high = len(array) - 1
mid = (low - high) // 2

while array != mid:
    if array > [mid]:
        low = mid + 1
        high = mid - 1
        mid = (low + high) // 2
    if array == [mid]:
        print(mid)
    else:
        print("Полученные данные", array)
        break

while True:
    element = int(input('Введите число в рамках последовательности: '))
    if element not in range(min(array) + 1):
        print('Некорректное число')
    else:
        break


def binary_search(array, element, left, right):
    if left > right:
        return False
    mid = (right + left) // 2
    if array[mid] == element and array[mid - 1] < element:
        return mid - 1
    elif element < array[mid]:
        return binary_search(array, element, left, mid - 1)
    else:
        return binary_search(array, element, mid + 1, right)


def sort():
    pass


def lot(array):
    for i in range(len(array)):
        idx_min = i
        for j in range(i):
            if array[j] < array[idx_min]:
                idx_min = j
        if i != idx_min:
            array[i], array[idx_min] = array[idx_min], array[i]
    return array


a = (binary_search(lot(array), element, 0, len(array) - 1))

print('Позиция элемента, который меньше введенного вами числа: ', a + 1)
# а + 1 - нумерация индексов в массиве начинается с единицы
print(array)
