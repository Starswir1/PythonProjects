nums = [10, 4, 8, 3]
leftSum = []
rightSum = []
answer = []
for num in range(0, len(nums)):
    a = sum(nums[:num])
    leftSum.append(a)
    b = sum(nums[num + 1:])
    rightSum.append(b)
    # for i in range(len(nums)):
    #     b = sum(nums[:i])
    #     rightSum.append(b)
    #     rightSum = rightSum[0:len(nums)]
    c = abs(leftSum[num] - rightSum[num])
    answer.append(c)
print(answer)
