def l_bin_search(l, r, l_val, seq):
    while l < r:
        m = (l + r) // 2
        if is_good_left(m, seq, l_val):
            r = m
        else:
            l = m + 1
    return l


def is_good_left(m, seq, l_val):
    return seq[m] >= l_val


def r_bin_search(l, r, r_val, seq):
    while l < r:
        m = (l + r + 1) // 2
        if is_good_right(m, seq, r_val):
            l = m
        else:
            r = m - 1
    return l


def is_good_right(m, seq, r_val):
    return seq[m] <= r_val

output_l = []

n = int(input())
seq = list(map(lambda x: int(x), input().split()))
seq.sort()
k = int(input())
if len(seq) == 1:
    for i in range(k):
        pair = list(map(lambda x: int(x), input().split()))
        if seq[0] in pair:
            output_l.append(1)
        else:
            output_l.append(0)
else:
    for i in range(k):
        pair = list(map(lambda x: int(x), input().split()))
        l_ind = l_bin_search(0, len(seq) - 1, pair[0], seq)
        r_ind = r_bin_search(0, len(seq) - 1, pair[1], seq)

        output_l.append(r_ind - l_ind + 1)

print(*output_l)
