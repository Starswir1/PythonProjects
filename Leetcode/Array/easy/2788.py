words = ["one.two.three", "four.five", "six"]
separator = "."
arr = ''
for word in words:
    arr = arr + "." + word
arr = arr.split(separator)
del arr[0]
print(arr)
