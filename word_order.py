def word_order(list1):
    dict1 = {}
    for i in list1:
        if i not in dict1:
            dict1[i] = 1
        else:
            dict1[i] += 1
    print(dict1)
    print(len(dict1))
    k = dict1.values()
    print(*k)


word_order(['bcdef','abcdefg','bcde','bcdef'])