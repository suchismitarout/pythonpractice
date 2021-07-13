def remove_k_digits(num, k):
    if len(num) <= k:
        return "0"
    res = [num[0]]
    for n in range(1, len(num)):
        while res and res[-1] > num[n] and k != 0:
            res.pop()
            k -= 1
        res.append(num[n])
    return str(int("".join(res))) if k == 0 else str(int("".join(res[:len(res) - k])))


print(remove_k_digits("1432219", 3))
