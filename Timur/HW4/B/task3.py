d = {}

with open("input.txt", "r") as f:
    for line in f:
        for word in line.split():
            if word not in d:
                d[word] = 0
            d[word] += 1

for k in sorted(d.items(), key=lambda pair: (-pair[1], pair[0])):
    print(k[0])

