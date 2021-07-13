def merge_sort_2_lists(list1, list2):
    num_list = [0] * (len(list1) + len(list2))
    i = j = k = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            num_list[k] = list1[i]
            i += 1
        else:
            num_list[k] = list2[j]
            j += 1
        k += 1

    while i < len(list1):
        num_list[k] = list1[i]
        i += 1
        k += 1

    while j < len(list2):
        num_list[k] = list2[j]
        j += 1
        k += 1

    return num_list


def merge_sort(num_list):
    if len(num_list) == 0:
        return num_list
    if len(num_list) == 1:
        return num_list[0]
    if len(num_list) == 2:
        return merge_sort_2_lists(num_list[0], num_list[1])
    mid = len(num_list)//2
    left = merge_sort(num_list[:mid])
    right = merge_sort(num_list[mid:])
    return merge_sort_2_lists(left,right)




num_list = [[1, 3, 5], [2, 6, 7], [4, 8, 9], [10,34,67]]
print(merge_sort(num_list))
