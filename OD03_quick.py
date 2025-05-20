def quick_sort(arr):
    """
    Быстрая сортировка.
    Рекурсивно делим массив на две части: меньше и больше опорного элемента.
    """
    if len(arr) <= 1:
        return arr  # базовый случай: массив из 0 или 1 элемента уже отсортирован

    pivot = arr[len(arr) // 2]  # выбираем опорный элемент (середина массива)
    left = [x for x in arr if x < pivot]      # всё, что меньше pivot
    middle = [x for x in arr if x == pivot]   # все элементы, равные pivot
    right = [x for x in arr if x > pivot]     # всё, что больше pivot

    # рекурсивно сортируем левую и правую часть
    return quick_sort(left) + middle + quick_sort(right)


print(quick_sort([5, 2, 9, 1, 5, 6]))  # [1, 2, 5, 5, 6, 9]