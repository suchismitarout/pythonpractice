def compress_the_string(string1):
    res = []
    counter = 1
    for i in range(1, len(string1)):
        r = string1[i - 1]
        if string1[i] != r:
            res.append((counter, r))
            counter = 1
        else:
            counter += 1
        if i == len(string1) - 1:
            res.append((counter, string1[i]))
    print(res)


compress_the_string('1222311112')
