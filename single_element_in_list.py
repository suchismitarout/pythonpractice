def single_element_in_list(list1):
    dict1 = {}
    for i in list1:
        if i not in dict1:
            dict1[i] = 1
        else:
            dict1[i] += 1
    for k,v in dict1.items():
        if v == 1:
            print(k)

single_element_in_list([3,3,7,7,10,11,11])