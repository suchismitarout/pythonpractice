def insertion_sort(list1):
    for i in range(1, len(list1)):
        key = list1[i]
        j = i - 1
        while j >= 0 and key < list1[j]:
            list1[j + 1] = list1[j]
            j -= 1
        list1[j + 1] = key
    print(list1)


l = [45, 3, 2, 4, 23, 12, 99, 25]

insertion_sort(l)
