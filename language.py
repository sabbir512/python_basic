import csv

with open("language.csv", "r") as file:
    reder = csv.DictReader(file)
    counts = {}
    for row in reder:
        lag = row["language"]
        if lag in counts:
            counts[lag] += 1
        else:
            counts[lag] = 1

def get_value(language):
    return counts[language]

for i in sorted(counts, key=get_value, reverse=True):
    print(f"{i}: {counts[i]}")