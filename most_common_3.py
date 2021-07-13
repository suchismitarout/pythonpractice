def most_common(input_string):
    dict1 = {}
    for i in input_string:
        if i not in dict1:
            dict1[i] = 1
        else:
            dict1[i] += 1

    s2 = sorted(sorted(dict1), key=dict1.get, reverse=True)
    first_3 = s2[:3]
    print(first_3)
    for i in first_3:
        print(i, dict1[i])

most_common('aabbbccde')

