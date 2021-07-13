def largest_number(nums):
    # nums.sort()
    nums.reverse()
    print(nums)
    res = ""

    for i in range(len(nums)):
        if lambda x, y: int(y + x) - int(x + y):
            res += str(nums[i])
    print(res)


largest_number([3, 30, 34, 5, 9])


k = [2,5,1,4,6]
l = list(filter(lambda x: x%2==0,k))
print(l)
