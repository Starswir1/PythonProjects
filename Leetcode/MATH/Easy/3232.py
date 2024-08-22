nums = [1, 2, 3, 5, 10]
a = 0
b = 0
for num in nums:

    if num < 10:
        a = num + a
    else:
        b = num + b
if a > b:
    print("lose")
else:
    print("win")
