nums = [1, 2, 3, 1, 1, 3]
c = 0
arr = []
for i in range(len(nums) - 1):  # 0, 1, 2, 3, 4
    a = nums[i]
    for j in range(i + 1, len(nums)):
        if a == nums[j]:
            c += 1
            arr.append(i)
            arr.append(j)
print(c)
print(arr)
