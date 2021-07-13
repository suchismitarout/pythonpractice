def majority_elements(nums):
    d = {}
    for i in nums:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    res = []
    for k, v in d.items():
        if v > len(nums) / 3:
            res.append(k)
    print(res)


majority_elements([3, 2, 3])
