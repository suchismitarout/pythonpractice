def count_and_say(digit):
    if digit == 1:
        return "1"
    if digit == 2:
        return "11"

    s = "11"
    for i in range(3, digit + 1):
        s += "$"
        res = ""
        counter = 1
        for j in range(1, len(s)):
            value = s[j-1]
            if s[j] != value:
                res += str(counter) + value
                counter = 1
            else:
                counter += 1
        s = res
    return s


print(count_and_say(6))
