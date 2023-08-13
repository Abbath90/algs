n = int(input())
l = map(lambda x: int(x), input().split())

ans = -10**9
cur_max = 0

for i in l:
    cur_max = max(cur_max + i, i)
    ans = max(ans, cur_max)

print(ans)
