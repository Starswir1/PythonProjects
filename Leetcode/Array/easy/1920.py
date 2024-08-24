nums = [0, 2, 1, 5, 3, 4]
ans = []
for i in nums:
    for j in range(len(nums)):
        a = nums[nums[j]]
        ans.append(a)
print(ans[:len(nums)])
