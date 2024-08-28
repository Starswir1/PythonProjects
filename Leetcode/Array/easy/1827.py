nums = [1, 5, 2, 4, 1]
i = 0
b = 0
for num in range(len(nums) - 1):
    while nums[i] >= nums[i + 1]:
        nums[i + 1] = nums[i + 1] + 1
        b = b + 1
    i = i + 1
print(b)
