def merge_the_tools(string1,k):
    t = []
    a = 0
    for i in string1:
        a +=1
        if i not in t:
            t.append(i)

        if a == k:
            print(''.join(t))
            t = []
            a = 0






merge_the_tools('AABCAAADA', 3)