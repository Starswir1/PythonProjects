import random

guess = [random.choice(range(1, 3)) for _ in range(3)]
answer = [random.choice(range(1, 3)) for _ in range(3)]
b = []
for i in range(len(guess)):
    a = bool(guess[i] == answer[i])
    b.append(a)
print(b)
print(guess)
print(answer)
