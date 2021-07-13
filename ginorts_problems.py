def is_sorted(a, b):
    if a is int and b.isalpha():
        return False
    elif b is int and a.isalpha():
        return True

    elif (a is int and b is int) and a < b and a % 2 != 0:
        return True
    elif (a is int and b is int) and a < b and a % 2 == 0:
        return False
    elif (a.isalpha() and b.isalpha()) and (a.islower() and b.isupper()):
        return True
    elif (a.isalpha() and b.isalpha()) and (a.isupper() and b.islower()):
        return False
    elif (a.isalpha() and b.isalpha()) and ord(a) < ord(b):
        return True
    else:
        return False


def replace_str_index(text, index=0, replacement=''):
    return '%s%s%s' % (text[:index], replacement, text[index + 1:])


def merge_sort(list1):
    if len(list1) > 1:
        mid = len(list1) // 2
        left = list1[:mid]
        right = list1[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if is_sorted(left[i], right[j]):
                # list1[k] = left[i]
                list1 = replace_str_index(list1, k, left[i])
                i += 1
            else:
                # list1[k] = right[j]
                list1 = replace_str_index(list1, k, right[j])
                j += 1
            k += 1

        while i < len(left):
            list1 = replace_str_index(list1, k, left[i])
            i += 1
            k += 1

        while j < len(right):
            list1 = replace_str_index(list1, k, right[j])
            j += 1
            k += 1
    return list1


def sorting_problem(string1):
    return merge_sort(string1)


print(sorting_problem('Sorting1234'))

print(sorted('Sorting1234'))


def sorting(string1):
    s = sorted(string1)
    l, u, o, e = [], [], [], []
    for i in s:
        if i.isalpha():
            x = u if i.isupper() else l
        else:
            x = o if int(i) % 2 else e
        x.append(i)
    print("".join(l + u + o + e))


sorting('Sorting1234')

