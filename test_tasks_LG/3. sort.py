# Быстрая сортировка Quicksort производит O(n*log(n)) обменов при упорядочении n элементов.

def quickSort(arr, first, second):
    f = first
    s = second
    pvt = arr[(f + s) // 2]

    while (f <= s):
        while (arr[f] < pvt):
            f += 1
        while (arr[s] > pvt):
            s -= 1
        if (f <= s):
            arr[f], arr[s] = arr[s], arr[f]
            f += 1
            s -= 1
        if (s > first):
            quickSort(arr, fist, s)
        if (f < second):
            quickSort(arr, f, second)

# Quicksort является одним из самых быстрых алгоритмов сортировки и превосходит другие алгоритмы.
