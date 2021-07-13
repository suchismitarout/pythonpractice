def insertion_sort(num_list):
    for i in range(len(num_list)):
        j = num_list[i]
        k = i-1
        while k >= 0 and num_list[k] > j:
            num_list[k+1] = num_list[k]
            k -= 1
        num_list[k+1] = j
    print(num_list)

insertion_sort([12,3,45,9,23,11,2])

