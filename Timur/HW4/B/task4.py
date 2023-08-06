parties = []
s = 0
s_after = 0
pos = 0

with open("input.txt", "r") as f:
    for line in f:
        l = line.split()
        key = " ".join(l[:-1])
        value = int(l[-1])
        parties.append([key, value, pos])
        s += value
        pos += 1

one_vote = s / 450

for i in parties:
    s_after += (i[1] // one_vote)
    i[1] = i[1] / one_vote
    i.append(i[1] % 1)

dif = 450 - s_after
parties.sort(key=lambda l: (l[3], l[1]), reverse=True)

if int(dif) != 450:
    for i in range(int(dif)):
        parties[i][1] += 1

parties.sort(key=lambda l: l[2])

for i in parties:
    print(i[0], int(i[1]) // 1)
