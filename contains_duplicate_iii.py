def contains_duplicates(num_list, k, t):
    res = {}
    for i in range(k):
        if num_list[i] not in res:
            res[num_list[i]] = 1
        else:
            res[num_list[i]] += 1
    print(res)


print(contains_duplicates([1, 2, 3, 1], k=3, t=0))
