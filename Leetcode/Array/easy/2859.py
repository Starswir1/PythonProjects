nums = [5, 10, 1, 5, 2]
k = 1
a = 0
for i in range(len(nums)):
    new_num = bin(i).replace('0b', '')
    substring = "1"
    count = new_num.count(substring)
    if count == k:
        a = nums[i] + a
print(a)
