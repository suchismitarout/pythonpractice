def convert_string_to_int(str1):
    res = 0
    for i in str1:
        res = res * 10
        for j in '012345789':
            res += i > j
    return res


def multiply_strings(st1, st2):
    st1 = convert_string_to_int(st1)
    st2 = convert_string_to_int(st2)
    print(str(st1 * st2))


multiply_strings("123", "456")
