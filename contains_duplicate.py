def contains_duplicate(num_list, k, t):
    for i in range(len(num_list)):
        for j in range(i+1, len(num_list)):
            if abs(num_list[i]-num_list[j]) <= t and abs(i-j) <=k:
                return True
    return False



print(contains_duplicate([1,5,9,1,5,9], k = 2, t = 3))
