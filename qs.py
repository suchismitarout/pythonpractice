def partition(list1, start, end):
    pivot = list1[start]
    low = start + 1
    high = end

    while True:
        while low <= high and list1[high] >= pivot:
            high = high - 1
        while low <= high and list1[low] <= pivot:
            low = low + 1

        if low <= high:
            list1[low], list1[high] = list1[high], list1[low]
        else:
            break
    list1[start], list1[high] = list1[high], list1[start]
    return high


def quick_sort(list1, start, end):
    if start >= end:
        return

    p = partition(list1, start, end)
    quick_sort(list1, start, p - 1)
    quick_sort(list1, p + 1, end)


list1 = [23, 11, 25, 19, 8, 34, 67, 45, 9, 2, 10]
quick_sort(list1, 0, len(list1) - 1)
print(list1)