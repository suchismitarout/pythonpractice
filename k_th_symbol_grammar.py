def kth_grammar(n,k):
    res = []
    res.append('0')
    for i in range(n):
        if '0' in res[i]:
            res.append('01')
        if '1' in res[i]:
            res.append('10')
    print(res)




kth_grammar(4,5)