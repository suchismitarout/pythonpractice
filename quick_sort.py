def partition(num_list, start, end):
    pivot = num_list[start]
    low = start + 1
    high = end
    while True:
        while low <= high and num_list[high] >= pivot:
            high = high - 1

        while low <= high and num_list[low] <= pivot:
            low = low + 1

        if low <= high:
            num_list[low], num_list[high] = num_list[high], num_list[low]
        else:
            break

    num_list[start], num_list[high] = num_list[high], num_list[start]
    return high


def quick_sort(num_list, start, end):
    if start >= end:
        return
    p = partition(num_list, start, end)
    quick_sort(num_list, start, p - 1)
    quick_sort(num_list, p + 1, end)


num_list = [29, 99, 27, 41, 66, 28, 44, 78, 87, 19, 31, 76, 58, 88, 83, 97, 12, 21, 44]
quick_sort(num_list, 0, len(num_list)-1)
print(num_list)
