def merge_sort(num_list):
    if len(num_list) > 1:
        length = len(num_list)
        mid = length // 2
        left_list = num_list[:mid]
        right_list = num_list[mid:]
        print("left:{}".format(left_list))
        print("right:{}".format(right_list))
        merge_sort(left_list)
        merge_sort(right_list)

        i = j = k = 0

        if i < len(left_list) and j < len(right_list):
            if i < len(left_list):
                num_list[k] = left_list[i]
                i += 1
            else:
                num_list[k] = right_list[j]
                j += 1
            k += 1

        if i < len(left_list):
            num_list[k] = left_list[i]
            i += 1
            k += 1
        if j < len(right_list):
            num_list[k] = right_list[j]
            j += 1
            k += 1


num_list = [6, 89, 1, 34, 8]
merge_sort(num_list)
print(num_list)

