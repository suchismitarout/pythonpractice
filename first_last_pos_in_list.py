def find_first_last_pos_in_sorted_list(list1, target):
    d = {}
    res = []
    if target not in list1:
        print([-1, -1])
    else:
        for i in range(len(list1)):
            if list1[i] not in d:
                d[list1[i]] = 1
            else:
                d[list1[i]] += 1
        for k, v in d.items():
            if k == target and v >= 1:
                res.append(list1.index(k))
                res.append(list1.index(k) + (v - 1))

        print(res)


find_first_last_pos_in_sorted_list([1], 1)


print(list(reversed([2,3,4])))


