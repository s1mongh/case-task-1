def sum_negative_between_max_min(A):
    # Найти индекс максимального и минимального элемента
    max_index = A.index(max(A))
    min_index = A.index(min(A))

    # Определить границы диапазона
    start = min(max_index, min_index)
    end = max(max_index, min_index)

    # Вычислить сумму отрицательных элементов между минимальным и максимальным
    negative_sum = sum(x for x in A[start + 1:end] if x < 0)

    return negative_sum


# Пример использования
A = [-6, -2, 3, -4, 5, -1, 7]
result = sum_negative_between_max_min(A)
print("Сумма отрицательных элементов между максимальным и минимальным:", result)
