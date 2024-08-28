names = ["Alice", "Bob", "Bob"]
heights = [155, 185, 150]
c = 0
# names = ["Mary", "John", "Emma"]
# heights = [180, 165, 170]
arr = []
for i in range(len(names)):
    a = max(heights)
    b = heights.index(a)
    arr.append(names[b])

    print("第", b, "个最高""为", arr[i])

    heights.remove(a)
    names.remove(names[b])
