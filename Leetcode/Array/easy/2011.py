x = 0
operations = ["--X", "X++", "X++"]
for operation in operations:
    if operation == "--X":
        x = x - 1
    elif operation == "X++":
        x = x + 1
print(x)
