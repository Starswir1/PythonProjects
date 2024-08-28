nums = [1, 15, 6, 3]
count = 0
count4 = 0
for num in nums:
    count += num
    if num < 10:
        count3 = num
    else:
        count1 = num % 10
        count2 = num // 10
        count3 = count2 + count1

    count4 = count3 + count4
    a = abs(count - count4)

print(a)
