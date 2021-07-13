def merge_sort(list1, r):
    if len(list1) > 1:
        mid = len(list1)//2
        left = list1[:mid]
        right = list1[mid:]
        merge_sort(left, r)
        merge_sort(right, r)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i][r] < right[j][r]:
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
    return list1

def athelete_sort(num_list, k):
    return merge_sort(num_list, k)

print(athelete_sort([[10, 2, 5], [7, 1, 0], [9, 9, 9], [1, 23, 12], [6, 5, 9]], 1))