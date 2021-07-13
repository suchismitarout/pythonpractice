def find_pattern(num_list):
    first_list = []
    sec_list = []
    for i in range(len(num_list)):
        if len(first_list) > 1:
            min_n = min(first_list)
        else:
            min_n = num_list[0]
        if i == 0:
            first_list.append(num_list[i])
        else:
            if num_list[i - 1] < num_list[i]:
                first_list.append(min_n)
            elif num_list[i] < min_n:
                first_list.append(num_list[i])
    for j in range(len(num_list) - 1, 0, -1):
        if num_list[j - 1] and num_list[j - 1] > num_list[j]:
            sec_list.append(num_list[j - 1])
    print("first list:{}".format(first_list))
    print("Sec list:{}".format(sec_list))


find_pattern([12, 3, 11, 4, 5, 6, 7, 2, 9, 10])



