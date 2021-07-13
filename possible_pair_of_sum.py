def possible_pair_of_sum(num_list, k):
    res = []
    while num_list:
        number = num_list.pop()
        diff = k - number
        if diff in num_list:
            res.append((diff, number))
    print(res)


possible_pair_of_sum([1, 5, 3, 7, 9], 12)
