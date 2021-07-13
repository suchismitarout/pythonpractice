def uglynumbers_ii(n):
    res = []
    for i in range(1,1690):
        if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
            res.append(i)

    print(res[0:n])



uglynumbers_ii(10)