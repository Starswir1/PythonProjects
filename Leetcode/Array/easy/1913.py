nums = [5, 6, 2, 7, 4]
a = max(nums)
b = min(nums)
nums.remove(a)
nums.remove(b)
c = max(nums)
d = min(nums)
e = (a * c - b * d)
print(e)
