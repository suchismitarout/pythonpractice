def find_pairs(list1, list2, k):
    r = []

    for i in range(len(list1)):
        for j in range(len(list2)):
            s = list1[i] + list2[j]
            r.append([s, [list1[i], list2[j]]])
    r = sorted(r)
    res = [x[1] for x in r[:k]]
    print(res)


find_pairs([1, 2, 4, 5, 6], [3, 5, 7, 9], 3)
