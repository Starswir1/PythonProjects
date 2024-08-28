heights = [1, 1, 4, 2, 1, 3]
arr = heights.copy()
arr.sort()
b = 0
for i in range(len(heights)):
    if heights[i] == arr[i]:
        b += 1
print(b)
