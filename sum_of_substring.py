def sum_of_substring(num_list, k):
    res = []
    for i in range(len(num_list)):
        diff = k - num_list[i]
        if diff in num_list:
            res.append([num_list[i], diff])

    print(res)


sum_of_substring([2, 1, 4, 5,3], 10)

