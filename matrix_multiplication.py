def matrix_multiplication(list1, list2):
    res = [[0 for x in range(len(list2[0]))]for y in range(len(list1))]
    print(res)
    for i in range(len(list1)):
        for j in range(len(list2[0])):
            for k in range(len(list2)):
                res[i][j] += list1[i][k]* list2[k][j]
    print(res)









matrix_multiplication([[1, 2, 3],[3, 4, 5],[7, 6, 4]], [[5, 2, 6, 1],[5, 6, 7, 2],[7, 6, 4, 3]])