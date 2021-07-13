def find_pairs(num_list, target):
    res = []
    while num_list:
        num = num_list.pop()
        diff = target - num
        if diff in num_list:
            res.append((diff, num))
    print(res)


find_pairs([1, 5, 3, 7, 9], 12)




