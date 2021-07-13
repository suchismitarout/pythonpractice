def print_all_elements_by_index(list1):
    max_length = len(max(list1, key=len))
    res = {}
    i = 0
    t = []
    while True:
        r = ""
        for j in range(len(list1)):
            try:
                r += list1[j][i]
            except IndexError:
                j += 1
        res[i] = r
        i += 1
        if i == max_length:
            break
    for k, v in res.items():
        t.append(v)
    print(t)


print_all_elements_by_index(['12345', '12', '123', '4322'])
