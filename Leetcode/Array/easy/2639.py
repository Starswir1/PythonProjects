grid = [[-15, 1, 3],
        [15, 7, 12],
        [5, 6, -2]]
arr = []
arr1 = []
for row in range(len(grid)):
    arr = []
    for col in range(len(grid[0])):
        arr.append(len(str(grid[col][row])))

    b = max(arr)
    arr1.append(b)
print(arr1)
# print(grid[0][1])
