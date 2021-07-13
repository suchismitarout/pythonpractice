def nth_ugly_number(n, a, b, c):
    r = []
    for i in range(1, n + 10):
        if i % a == 0 or i % b == 0 or i % c == 0:
            r.append(i)

    for i in range(len(r)):
        if i == n:
            print(r[i - 1])


nth_ugly_number(n=1000000000, a=2, b=217983653, c=336916467)
