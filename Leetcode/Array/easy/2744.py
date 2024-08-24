words = ["cd", "ac", "dc", "ca", "zz"]
b = 0
for word in words:

    arranged = "".join(sorted(word))
    if arranged != word:
        b = b + 1
print(b)
