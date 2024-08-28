words = ["pay", "attention", "practice", "attend"]
pref = "at"
b = 0
for word in words:
    if word[:len(pref)] == pref:
        b += 1
print(b)
