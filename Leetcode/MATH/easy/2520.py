def count_divisible_digits(num):
    count = 0
    newnum = str(num)
    for char in newnum:
        char1 = int(char)
        if num % char1 == 0:
            count += 1
    return count


# 示例
num = 123
print(count_divisible_digits(num))  # 输出能整除num的数位的数目
