numbers = [2, 7, 11, 15]
target = 9
left, right = 0, len(numbers) - 1


def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    left, right = 0, len(numbers) - 1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]
        elif total < target:
            left += 1
        else:
            right -= 1
    return [-1, -1]


print(twoSum(numbers, target))
