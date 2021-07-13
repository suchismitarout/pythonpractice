def sublist_from_list(list1, target):
    res = []
    for i in range(1, len(list1)):
        if i + 1 < len(list1):
            prev = list1[i - 1]
            nex = list1[i + 1]
            if list1[i] + prev + nex == target:
                res.append([prev, list1[i], nex])
    print(res)


sublist_from_list([3, 4, 2, 6, 1, 5, 3], 12)
