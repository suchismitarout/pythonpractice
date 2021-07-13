
def piling_up(n, list1):
    for t in range(n):
        min_list = list1.index(min(list1))
        left = list1[:min_list]
        right = list1[min_list + 1:]
        print(left)
        print(right)
        if left == sorted(left, reverse=True) and right == sorted(right):
            print("Yes")
        else:
            print("No")


piling_up(1, [4,3,2,1,3,4])
piling_up(1, [1,2,3,8,7])