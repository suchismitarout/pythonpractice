def product_of_list_except_self(n):
    mul = 1
    r = {}
    for i in range(len(n)):
        if n[i] == 0:
            r[i] = n[i]
            pass
        else:
            mul *= n[i]
    if 0 in n:
        for i in range(len(n)):
            if i in r.keys() and len(n) == len(r):
                n[i] = 0
            elif i in r.keys() and len(n) != len(r):
                n[i] = mul
            else:
                n[i] = 0
    else:
        for i in range(len(n)):
            n[i] = mul // n[i]

    print(r)
    print(n)



product_of_list_except_self([-1, 1, 0, -3, 3])
# product_of_list_except_self([1,2,3,4])
# product_of_list_except_self([0,0])