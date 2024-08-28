rectangles = [[5, 8], [3, 9], [5, 12], [16, 5]]
arr = []
for rectangle in rectangles:
    a = min(rectangle)
    arr.append(a)
    b = max(arr)
c = arr.count(b)
print(arr)
print(c)
