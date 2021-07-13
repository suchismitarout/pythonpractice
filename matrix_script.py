def matrix_script(list1, k):
    res = []
    t = ['!','@','#','$','%','&']
    for i in range(k):
        r = ''
        for j in list1:
            p = j[i]
            if p in t:
                j.replace(p,'')
            else:
                r += p
        res.append(r)
    print(''.join(res))




matrix_script(['Tsi', 'h%x', 'i #', 'sM ', '$a ', '#t%', 'ir!'], 3)