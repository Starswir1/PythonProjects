words = ["abc", "car", "ada", "racecar", "cool"]
arr = []
for word in words:
    if word == word[::-1]:
        arr.append(word)
print(arr[0])
