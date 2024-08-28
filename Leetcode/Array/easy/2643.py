mat = [[0, 0], [1, 1], [0, 0]]
b = 0
arr = []
arr1 = []
for i in range(len(mat)):
    a = mat[i].count(1)
    arr.append(a)
if max(arr) == min(arr):
    b = arr.index(max(arr))
    arr1.append(b)
else:
    b = max(arr)
    c = arr.index(max(arr))
    arr1.append(c)
    arr1.append(b)
print(arr1)
