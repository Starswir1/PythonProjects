grid = [[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]
maxLocal = []
a = grid[0][0]
for row in range(0, 3):
    for col in range(0, 3):
        if grid[row][col] > a:
            a = grid[row][col]
        maxLocal[row][col] = a
print(maxLocal)
