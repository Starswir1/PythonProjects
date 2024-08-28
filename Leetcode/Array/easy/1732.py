arr = [0]
gain = [-5, 1, 5, 0, -7]
i = 0
for num in gain:
    a = num + arr[i]
    arr.append(a)
    i = i + 1
print(arr)
