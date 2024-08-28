nums = [13, 25, 83, 77]
arr = []
i = 0
for num in nums:
    string1 = str(num)
    if len(string1) == 5:
        a = int(string1[0])
        b = int(string1[1])
        c = int(string1[2])
        d = int(string1[3])
        e = int(string1[4])
        arr.append(a)
        arr.append(b)
        arr.append(c)
        arr.append(d)
        arr.append(e)
    elif len(string1) == 4:
        a = int(string1[0])
        b = int(string1[1])
        c = int(string1[2])
        d = int(string1[3])
        arr.append(a)
        arr.append(b)
        arr.append(c)
        arr.append(d)

    elif len(string1) == 3:
        a = int(string1[0])
        b = int(string1[1])
        c = int(string1[2])
        arr.append(a)
        arr.append(b)
        arr.append(c)

    elif len(string1) == 2:
        a = int(string1[0])
        b = int(string1[1])
        arr.append(a)
        arr.append(b)

    elif len(string1) == 1:
        a = int(string1[0])
        arr.append(a)

print(arr)
