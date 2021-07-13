def removeDuplicateLetters(s):
    dict1 = {char: index for index, char in enumerate(s)}
    res = []

    for index, char in enumerate(s):
        if char not in res:
            while res and index < dict1[res[-1]] and char < res[-1]:
                res.pop()
            res.append(char)
    return ''.join(res)


print(removeDuplicateLetters("cbacdcbc"))
