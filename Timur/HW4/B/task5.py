def find_max_key_by_val(d):
    m = max(d.values())
    for key, value in d.items():
        if m == value:
            return key

d = {}
cnt_d = {}

n = int(input())

l = [0] * n

for i in range(n):
    mes = int(input())
    if mes == 0:
        d[input()] = i
        l[i] = i
        input()
    else:
        l[i] = l[mes - 1]
        input()


for i in l:
    if i not in cnt_d:
        cnt_d[i] = 0
    cnt_d[i] += 1

m = find_max_key_by_val(cnt_d)

for key, value in d.items():
    if m == value:
        print(key)
