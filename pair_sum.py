def sum_of_pairs(list1, target):
    num_set = set()
    res = []
    for i in list1:
        diff = target - i
        if diff not in num_set:
            num_set.add(i)
        else:
            res.append([diff, i])
    print(res)

sum_of_pairs([4, 5, 3, 2, 1, 7], 6)
