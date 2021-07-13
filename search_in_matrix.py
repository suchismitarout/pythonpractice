def search_in_2d_matrix(list1, target):
    r = True
    for i in list1:
        if target in i:
            r = True
            break
        else:
            r = False

    return r


print(search_in_2d_matrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13))
# print(search_in_2d_matrix([[1], [3]], 3))
