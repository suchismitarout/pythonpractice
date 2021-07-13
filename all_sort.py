###############
# merge sort  #
###############
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


num_list = [23, 12, 45, 22, 26, 78, 1, 34, 7]

merge_sort(num_list)
print(num_list)


###############
# quick sort  #
###############
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
            num_list[high], num_list[low] = num_list[low], num_list[high]

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


n = [23, 12, 45, 22, 26, 78, 1, 34, 7]
quick_sort(n, 0, len(n) - 1)
print(n)


################
# Bubble sort  #
################

def bubble_sort(num_list):
    for i in range(len(num_list)):
        for j in range(i + 1, len(num_list)):
            if num_list[i] > num_list[j]:
                num_list[i], num_list[j] = num_list[j], num_list[i]
    return num_list


print(bubble_sort([23, 12, 45, 22, 26, 78, 1, 34, 7]))


###################
# Selection sort  #
###################

def selection_sort(num_list):
    for i in range(len(num_list)):
        min_num = i
        for j in range(i + 1, len(num_list)):
            if num_list[min_num] > num_list[j]:
                min_num = j
        num_list[i], num_list[min_num] = num_list[min_num], num_list[i]
    return num_list


print(selection_sort([23, 12, 45, 22, 26, 78, 1, 34, 7]))


###################
# Insertion sort  #
###################

def insertion_sort(num_list):
    for i in range(1, len(num_list)):
        k = num_list[i]
        j = i - 1
        while j >= 0 and k < num_list[j]:
            num_list[j + 1] = num_list[j]
            j -= 1
        num_list[j + 1] = k
    return num_list


print(insertion_sort([23, 12, 45, 22, 26, 78, 1, 34, 7]))


###################
# Min heap sort   #
###################

def minheapify(num_list, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and num_list[smallest] < num_list[left]:
        smallest = left

    if right < n and num_list[smallest] < num_list[right]:
        smallest = right

    if smallest != i:
        num_list[i], num_list[smallest] = num_list[smallest], num_list[i]
        minheapify(num_list, n, smallest)


def minheapsort(num_list):
    n = len(num_list)

    for i in range(n // 2, -1, -1):
        minheapify(num_list, n, i)
    for i in range(n - 1, -1, -1):
        num_list[0], num_list[i] = num_list[i], num_list[0]
        minheapify(num_list, i, 0)


k = [23, 12, 45, 22, 26, 78, 1, 34, 7]
minheapsort(k)

n = len(k)
print("Sorted array is")
for i in range(n):
    print("%d " % k[i], end='')


# ###################
# # Max heap sort   #
# ###################
#
# def maxheapify(num_list, n, i):
#     largest = i
#     left = 2*i + 1
#     right = 2*i + 2
#     if left < n and num_list[left] > largest:
#         largest = left
#     if right < n and num_list[right] > largest:
#         largest = right
#     if largest != i:
#         num_list[i], num_list[largest] = num_list[largest], num_list[i]
#         maxheapify(num_list, n, largest)
#
#
# def maxheapsort(num_list):
#     n = len(num_list)
#
#     for i in range(n // 2 - 1, -1, -1):
#         maxheapify(num_list, n, i)
#     for i in range(n - 1, -1, -1):
#         num_list[0], num_list[i] = num_list[i], num_list[0]
#         maxheapify(num_list, i, 0)
#
#
# l = [23, 12, 45, 22, 26, 78, 1, 34, 7]
# maxheapsort(l)
#
# n = len(l)
# print("\n")
# print("Sorted array is")
# for i in range(n):
#     print("%d " % l[i], end='')
