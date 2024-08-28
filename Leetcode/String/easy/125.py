s = "race a car"


def isPalindrome(s):
    left, right = 0, len(s) - 1
    s = "".join(ch for ch in s if ch.isalnum()).lower()
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1


        else:
            return False
    return True


print(isPalindrome(s))
