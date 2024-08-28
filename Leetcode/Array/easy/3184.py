hours = [72, 48, 24, 3]
i = 0
b = 0
for i in range(len(hours)):
    for j in range(i + 1, len(hours)):
        if (hours[i] + hours[j]) % 24 == 0:
            b = b + 1
            print(i, j)
print(b)
