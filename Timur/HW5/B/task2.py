n = int(input())
l = list(map(lambda x: int(x), input().split()))

prefix_sum_l = [0]*(n + 1)

for i in range(1, n + 1):
    prefix_sum_l[i] = prefix_sum_l[i - 1] + l[i - 1]


print(prefix_sum_l)
