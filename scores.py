# score = [72, 73, 33]

# avarage = sum(score) / len(score)
# print(f"Avarage: {avarage}")

from cs50 import get_int

scores = []

for i in range(3):
    score = get_int("Get input: ")
    scores.append(score)

avarage = sum(scores) / len(scores)
print(f"Avarage: {avarage}")
