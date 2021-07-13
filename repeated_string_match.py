def repeated_string_match(str1, str2):
    a = str1

    def repeated_str_match(str1, str2, count):
        if len(str2) + len(a) < len(str1) and str2 not in str1: return -1
        if str2 in str1: return count
        return repeated_str_match(str1 + a, str2, count + 1)

    return repeated_str_match(str1, str2, 1)


print(repeated_string_match("abc", "wxyz"))
