nums = [1, 2, 3, 4]
arr = []
for i in range(len(nums) + 1):
    if len(nums) % (i + 1) == 0:
        arr.append(nums[i])


def sum_squares(nums):
    sum = 0
    for i in range(len(nums)):
        sum += nums[i] * nums[i]
    return sum


print(sum_squares(arr))
