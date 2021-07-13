def power_of_two(input_num):
    if input_num == 0:
        return False
    while input_num != 1:
        if input_num % 2 != 0:
            return False
        input_num = input_num // 2
    return True


print(power_of_two(24))


def count_good_meals(input_list):
    count = 0
    res = []
    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list)):
            k = input_list[i] + input_list[j]
            if power_of_two(k):
                res.append((input_list[i], input_list[j]))
                count += 1
    print(count)
    print(res)


count_good_meals([1, 1, 1, 3, 3, 3, 7])
