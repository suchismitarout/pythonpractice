def merge_sort(list1, list2,n1, n2):
    final_list = [0]*(n1+n2)
    i = j = k = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            final_list[k] = list1[i]
            i += 1
        else:
            final_list[k] = list2[j]
            j += 1
        k += 1

    while i < len(list1):
        final_list[k] = list1[i]
        i += 1
        k += 1

    while j < len(list2):
        final_list[k] = list2[j]
        j += 1
        k += 1

    return final_list


list1 = [1, 4, 6]
list2 = [2, 5, 7]
list3 = [3, 8, 9]
n1 = len(list1)
n2 = len(list2)
n3 = len(list3)
first = merge_sort(list1, list2, n1, n2)
second = merge_sort(first,list3, n1+n2, n3)
print(second)

