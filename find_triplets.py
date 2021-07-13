def sum_of_triplets(list1, target):
    num_set = set()
    res = []
    for i in range(len(list1)):
        for j in range(i+1, len(list1)):
            diff = target - (list1[i]+list1[j])
            if diff not in num_set:
                num_set.add(list1[i])
                num_set.add(list1[j])
            else:
                res.append([list1[i],list1[j], diff])
    print(res)







sum_of_triplets([2,5,3,6,7,8,1,9],18)