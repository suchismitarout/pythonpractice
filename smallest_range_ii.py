def smallest_range(a, k):
    n = len(a)
    b = []
    for i in range(len(a)-1):
        b.append(a[i] + k)

    b.append(a[n-1]-k)
    print(a)
    print(b)
    print(max(b))

    print(max(b)-min(b))


smallest_range([2, 7, 2], 1)
