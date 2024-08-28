words = ["a", "b", "c", "ab", "bc", "abc"]
s = "abc"
b = 0
for w in words:
    for c in s:
        if w == c:
            b = b + 1
print(b)
