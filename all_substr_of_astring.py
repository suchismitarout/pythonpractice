def subString(s, n):
    st = 0
    k = 0
    for i in range(n):
        for len in range(i + 1, n + 1):
            # print(s[i: len])
            t = s[i:len]

            if t[0] in ('a', 'e', 'i', 'o', 'u'):
                k = k + 1
            else:
                st = st + 1
    print(st)
    print(k)
s = "banana"
subString(s, len(s))
def all_substrings_from_string(string1):
    stuart = 0
    kevin = 0
    vowels = 'AEIUO'
    for i in range(len(string1)):
        if string1[i] in vowels:
            kevin += len(string1)-i
        else:
            stuart += len(string1)-i

    print(stuart)
    print(kevin)

all_substrings_from_string("BANANA")