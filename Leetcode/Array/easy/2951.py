mountain = [1, 4, 3, 8, 5]
arr = []
j = 0
for i in range(len(mountain)):
    if len(mountain) <= 2 and i == len(mountain) - 1:
        print("none")
        break
    if mountain[i + 1] > mountain[i] and mountain[i + 2] < mountain[i + 1] and i:
        arr.append(i)

print(arr)
