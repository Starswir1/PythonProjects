encoded = [1, 2, 3]
first = 1

arr = []
arr.append(first)
for i in range(1, len(encoded) + 1):
    a = arr[i - 1] ^ encoded[i - 1]
    arr.append(a)
print(arr)
