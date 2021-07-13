def divisible_by_p(num_list, p):
    if sum(num_list) % p == 0:
        return 0
    else:
        count = 0
        for i in range(len(num_list)):
            num_list.pop()
            if sum(num_list) % p == 0:
                count += 1
                return count


print(divisible_by_p([3, 1, 4, 2], 6))


