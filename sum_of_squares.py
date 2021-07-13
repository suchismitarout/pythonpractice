def sum_of_squares(digit):
    if digit == 1:
        return True
    is_exists = True
    for i in range(digit):
        sum1 = 0
        for j in range(digit):
            sum1 = (i * i) + (j * j)
            if sum1 == digit:
                is_exists = True
                return is_exists
            else:
                is_exists = False
    return is_exists


print(sum_of_squares(5))
