def possible_triplet_of_sum(num_list, k):

    for i in range(len(num_list) - 1):
        s = set()
        diff = k - num_list[i]
        for j in range(i + 1, len(num_list)):
            if diff - num_list[j] in s:
                print((num_list[i], num_list[j], diff - num_list[j]))
                return True
            s.add(num_list[j])
    return False


print(possible_triplet_of_sum([1, 4, 45, 6, 10, 8], 22))
