n = int(input())
n_seq = list(map(lambda x: int(x), input().split()))
m = int(input())
m_seq = map(lambda x: int(x), input().split())
length_n_seq = len(n_seq)


def l_bin_search(l, r, val):
    while l < r:
        m  = (l + r) // 2
        if is_good_left(m, val):
            r = m
        else:
            l = m + 1
    return l


def is_good_left(m, val):
    return n_seq[m - 1] >= val


def r_bin_search(l, r, val):
    while l < r:
        m  = (l + r + 1) // 2
        if is_good_right(m, val):
            l = m
        else:
            r = m - 1
    return l


def is_good_right(m, val):
    return n_seq[m - 1] <= val


for i in m_seq:
    if i not in n_seq:
        print(0, 0)
    else:
        l_ind = l_bin_search(1, length_n_seq, i)
        r_ind = r_bin_search(1, length_n_seq, i)
        print(l_ind, r_ind)
