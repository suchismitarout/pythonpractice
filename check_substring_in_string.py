def substring_in_string(full_string, sub_string):
    start = 0
    end = 0
    while start < len(full_string):
        if full_string[start + end] != sub_string[end]:
            start += 1
            end = 0
            continue
        end += 1
        if end == len(sub_string):  
            return start
    return -1


print(substring_in_string("dedicate", "cat"))


def check_substring(string1, sub_str):
    start = 0
    end = 0
    while start < len(string1):
        if string1[start+end] != sub_str[end]:
            start += 1
            end = 0
            continue
        end += 1
        if end == len(sub_str):
            return True
    return False


print(check_substring("dedicate", "cat"))