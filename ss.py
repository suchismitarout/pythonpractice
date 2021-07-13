def partition(num_list, start, end):
    pivot = num_list[start]
    low = start + 1
    high = end

    while True:
        while low <= high and num_list[high] > pivot:
            high = high - 1
        while low <= high and num_list[low] < pivot:
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


num_list = [12, 1, 34, 23, 11, 3, 56, 7]
quick_sort(num_list, 0, len(num_list) - 1)
print(num_list)


def selection_sort(num_list):
    for i in range(len(num_list)):
        min_n = i
        for j in range(i + 1, len(num_list)):
            if num_list[min_n] > num_list[j]:
                min_n = j
        num_list[i], num_list[min_n] = num_list[min_n], num_list[i]
    print(num_list)


selection_sort([12, 1, 34, 23, 11, 3, 56, 7])


def merge_sort(num_list):
    if len(num_list) > 1:
        mid = len(num_list) // 2
        left = num_list[:mid]
        right = num_list[mid:]
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                num_list[k] = left[i]
                i += 1
            else:
                num_list[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            num_list[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            num_list[k] = right[j]
            j += 1
            k += 1


num_list = [12, 1, 34, 23, 11, 3, 56, 7]
merge_sort(num_list)
print(num_list)


def insertion_sort(num_list):
    for i in range(1, len(num_list)):
        k = num_list[i]
        j = i - 1
        while j >= 0 and k < num_list[j]:
            num_list[j + 1] = num_list[j]
            j -= 1
        num_list[j + 1] = k
    return num_list


print(insertion_sort([12, 1, 34, 23, 11, 3, 56, 7]))


def heapify(num_list, n, i):
    largest = i
    left = i * 2 + 1
    right = i * 2 + 2

    if left < n and num_list[largest] < num_list[left]:
        largest = left

    if right < n and num_list[largest] < num_list[right]:
        largest = right

    if largest != i:
        num_list[i], num_list[largest] = num_list[largest], num_list[i]
        heapify(num_list, n, largest)

def heap_sort(num_list):
    n = len(num_list)
    for i in range(n//2-1, -1, -1):
        heapify(num_list, n, i)

    for j in range(n-1, 0, -1):
        num_list[j], num_list[0] = num_list[0], num_list[j]
        heapify(num_list, j, 0)


n = [12, 1, 34, 23, 11, 3, 56, 7]
heap_sort(n)
print(n)