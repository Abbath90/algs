observers = int(input())
observations = []
for i in range(observers):
    observations.append(input())

n = int(input())
numbers = []
numbers_with_cnt = []
for i in range(n):
    numbers.append(input())

max_cnt = 0
for i in numbers:
    m = [i, 0]
    for j in observations:
        if len(set(j).difference(set(i))) == 0:
            m[1] += 1
    numbers_with_cnt.append(m)
    if m[1] > max_cnt:
        max_cnt = m[1]

print(*[num for num, cnt in numbers_with_cnt if cnt == max_cnt], sep="\n")
