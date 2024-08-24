s = "hello"
count = 0
for i in range(0, len(s) - 1):
    # 0,1,2,3
    a = ord(s[i])
    b = ord(s[i + 1])
    c = abs(b - a)

    count = count + c

print(count)
