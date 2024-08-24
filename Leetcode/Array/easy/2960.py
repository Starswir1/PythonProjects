batteryPercentages = [1, 1, 2, 1, 3]
b = 0
for i in range(0, len(batteryPercentages)):
    if batteryPercentages[i] > 0:
        b += 1
        batteryPercentages = [j - 1 for j in batteryPercentages]
    elif batteryPercentages[i] == 0:
        continue
print(b)
