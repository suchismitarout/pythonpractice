def threeSum(nums):
    nums.sort()
    result = set()
    for i in range(len(nums) - 2):
        l = i + 1
        r = len(nums) - 1
        while (l < r):
            sum = nums[i] + nums[l] + nums[r]
            if sum < 0:
                l += 1
            elif sum > 0:
                r -= 1
            else:
                result.add(tuple([nums[i], nums[l], nums[r]]))
                while l < len(nums) - 1 and nums[l] == nums[l + 1]: l += 1
                while r > 0 and nums[r] == nums[r - 1]: r -= 1
                l += 1
                r -= 1
    return [list(res) for res in list(result)]

k = threeSum([-1,0,1,2,-1,-4])
print(k)