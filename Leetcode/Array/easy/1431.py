candies = [2, 3, 5, 1, 3]
arr = []
extraCandies = 3
for candie in candies:
    a = extraCandies + candie
    b = bool(a >= max(candies))
    arr.append(b)
print(arr)
