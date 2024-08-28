# nums = [1, 5, 4, 5]
nums = [3, 4, 7, 2, 5, 6]
a = max(nums)
arr = []
b = nums[0]
for i in range(len(nums) - 1):
    if nums[i] < nums[i + 1]:
        b = nums[i + 1]
        arr.append(b)
print(arr)
