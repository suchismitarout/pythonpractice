def reverse_string(string1):
    stk = []
    l = ''
    for i in string1:
        stk.append(i)
    for i in range(len(stk)):
        l += stk.pop()
    return l

# reverse_string("hello")


def reverse_words_in_list(string1):
    list1 = string1.split()
    res = []
    for i in range(len(list1)):
        r = reverse_string(list1[i])
        res.append(r)
    print(' '.join(res))




reverse_words_in_list('you are awesome')