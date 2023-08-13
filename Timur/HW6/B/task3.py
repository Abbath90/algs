a, day_off_a, b, day_off_b, x = list(map(lambda x: int(x), input().split()))


def l_bin_search(l, r, a, day_off_a, b, day_off_b, x):
    while l < r:
        m = (l + r) // 2
        if (m - m // day_off_a) * a + (m - m // day_off_b) * b >= x:
            r = m
        else:
            l = m + 1
    return l

r = 2 * x // 2 + 1

ans = l_bin_search(0, r, a, day_off_a, b, day_off_b, x)
print(ans)

