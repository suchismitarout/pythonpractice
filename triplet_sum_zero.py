def find_triplet_sum_zero(num_list):
    if len(num_list) > 1:
        res = []
        num_list.sort()
        for num in range(len(num_list)):
            for num1 in range(num + 1, len(num_list)):
                for num2 in range(num1 + 1, len(num_list)):
                    if num_list[num] + num_list[num1] + num_list[num2] == 0:
                        if [num_list[num], num_list[num1], num_list[num2]] not in res:
                            res.append([num_list[num], num_list[num1], num_list[num2]])
        return res
    else:
        return []


print(find_triplet_sum_zero([-1, 0, 1, 2, -1, -4]))


# print(find_triplet_sum_zero([0]))


def find_triplet_sum(num_list):
    if len(num_list) > 1:
        p = []
        for i in range(len(num_list) - 1):
            s = dict()
            for j in range(i + 1, len(num_list)):
                k = 0 - (num_list[i] + num_list[j])
                if k in s.keys() and num_list[i] and num_list[j] not in s.keys():
                    p.append([k, num_list[i], num_list[j]])
                else:
                    s[num_list[j]] = 1
        return p
    else:
        return []


print(find_triplet_sum([0,0,0]))
