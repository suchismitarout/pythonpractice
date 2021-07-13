def quadsum(list1, sum1):
    if len(list1) < 1:
        return []
    else:
        list1.sort()
        res = set()
        for i in range(len(list1)-3):
            for j in range(i+1, len(list1)-2):
                diff = sum1 - (list1[i] + list1[j])
                low = j + 1
                high = len(list1)-1
                while low < high:
                    if list1[low] + list1[high] < diff:
                        low += 1
                    elif list1[low] + list1[high] > diff:
                        high -= 1
                    else:
                        res.add((list1[i], list1[j], list1[low], list1[high]))
                        (low, high) = (low+1, high-1)
    r = [list(x) for x in res]
    print(r)

quadsum([-2,-1,-1,1,1,2,2], 0)

