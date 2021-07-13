def single_number_iii(num_list):
    dict1 = {}
    res = []
    for i in num_list:
        if i not in dict1:
            dict1[i] = 1
        else:
            dict1[i] += 1
    for k,v in dict1.items():
        if v == 1:
            res.append(k)
    print(res)



# single_number_iii([1,2,1,3,2,5])
single_number_iii([0,1])