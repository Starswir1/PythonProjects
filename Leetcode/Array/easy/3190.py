nums = [1, 2, 3, 4]
i = 0
b = 0
for num in nums:
    if num % 3 == 1:
        b += 1
    if num % 3 == 2:
        b += 1
print(b)
print(nums)
