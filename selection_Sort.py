def selection_sort(num_list):
    for i in range(len(num_list)):
        min_num = i
        for j in range(i + 1, len(num_list)):
            if num_list[min_num] > num_list[j]:
                min_num = j
        num_list[i], num_list[min_num] = num_list[min_num], num_list[i]
    print(num_list)


selection_sort([23, 11, 29, 8, 25, 43, 18])
