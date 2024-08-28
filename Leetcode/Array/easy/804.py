words = ["gin", "zen", "gig", "msg"]
code = [".-", "-...", "-.-.", "-..", ".",
        "..-.", "--.", "....", "..", ".---",
        "-.-", ".-..", "--", "-.", "---", ".--.",
        "--.-", ".-.", "...", "-", "..-",
        "...-", ".--", "-..-", "-.--", "--.."]
arr1 = []
b = 0
d = 0
for word in words:
    c = ''
    for i in word:
        a = ord(i)
        b = code[a - 97]
        c = c + b
    arr1.append(c)
for i in range(len(arr1) - 1):
    if arr1[i] == arr1[i + 1]:
        d += 1
print(d)
