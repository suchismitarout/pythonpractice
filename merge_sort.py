def merge_sort(num_list):
    if len(num_list) > 1:
        mid = len(num_list) // 2
        left = num_list[:mid]
        right = num_list[mid:]
        # print("left:{}".format(left))
        # print("right:{}".format(right))
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


num_list = [67,1,23,45,10,23,34,11]
merge_sort(num_list)
print(num_list)
