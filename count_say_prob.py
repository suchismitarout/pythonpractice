def count_say(n):
    if n == 1:
        return '1'
    if n == 2:
        return '11'
    s = '11'
    for i in range(3, n+1):
        res = ''
        s += '$'
        counter = 1
        for j in range(1,len(s)):
            value = s[j-1]
            if s[j] != value:
                res += str(counter) + value
                counter = 1
            else:
                counter += 1
        s = res
    return s
print(count_say(4))








count_say(5)