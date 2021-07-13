import math

def divide_integers(dividend, divisor):
    cur = -1 if (dividend < 0 or divisor < 0) else 1
    temp = 0
    dividend = abs(dividend)
    divisor = abs(divisor)

    print(math.floor(cur * math.exp(math.log(dividend) -
                               math.log(divisor))))
    # while dividend >= divisor:
    #     dividend -= divisor
    #     temp += 1
    # print(cur * temp)



divide_integers(-2147483648, -1)
