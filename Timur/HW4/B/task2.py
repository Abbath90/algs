d = {}

with open("input.txt", "r") as f:
    for line in f:
        candidate, votes = line.split()
        if candidate not in d:
            d[candidate] = 0
        d[candidate] += int(votes)

for k in sorted(d.keys()):
    print(k, d[k])