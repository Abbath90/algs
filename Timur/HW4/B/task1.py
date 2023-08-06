n = int(input())

d = {}
for i in range(n):
    l = list(map(lambda i: int(i), input().split()))
    if l[0] not in d:
        d[l[0]] = 0
    d[l[0]] += l[1]

for key in sorted(d.keys()):
    print(key, d[key])
