n = 10
m = 3
k = 0
q = 0
for i in range(1, n + 1):
    if i % m == 0:
        k = k + i
    else:
        q = q + i
print(q - k)
