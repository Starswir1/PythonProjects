nums = [5, 4, 2, 3]
arr = []
for num in nums:
    x = min(nums)
    nums.remove(x)
    y = min(nums)
    nums.remove(y)
    arr.append(y)
    arr.append(x)
print(arr)
