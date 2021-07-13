def merge_sort(list1):
    if len(list1) > 1:
        mid = len(list1) // 2
        left = list1[:mid]
        right = list1[mid:]

        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                list1[k] = left[i]
                i += 1
            else:
                list1[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            list1[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            list1[k] = right[j]
            j += 1
            k += 1


n_list = [45, 3, 12, 5, 34, 19, 7]
merge_sort(n_list)
print(n_list)


# quick_sort

def partition(list1, start, end):
    pivot = list1[start]
    low = start + 1
    high = end

    while True:
        while low <= high and list1[high] > pivot:
            high = high - 1
        while low <= high and list1[low] < pivot:
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


n_list = [12, 2, 24, 10, 8, 45]
quick_sort(n_list, 0, len(n_list) - 1)
print(n_list)


# selection sort

def selection_sort(list1):
    for i in range(len(list1)):
        m = i
        for j in range(i + 1, len(list1)):
            if list1[m] > list1[j]:
                m = j
        list1[i], list1[m] = list1[m], list1[i]


n_l = [12, 33, 2, 45, 8, 17]
selection_sort(n_l)
print(n_l)


# insertion_sort

def insertion_sort(list1):
    for i in range(1, len(list1)):
        j = list1[i]
        k = i - 1
        while k >= 0 and j < list1[k]:
            list1[k + 1] = list1[k]
            k -= 1
        list1[k + 1] = j
    print(list1)


insertion_sort(n_l)
