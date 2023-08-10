n, q = map(lambda i: int(i), input().split())

l = list(map(lambda i: int(i), input().split()))

cum_sum_l = [0]*(n + 1)
for i in range(1, n + 1):
    cum_sum_l[i] = cum_sum_l[i - 1] + l[i - 1]

for i in range(q):
    reql, reqr = map(lambda i: int(i), input().split())
    print(cum_sum_l[reqr] - cum_sum_l[reql-1])

print(cum_sum_l)
