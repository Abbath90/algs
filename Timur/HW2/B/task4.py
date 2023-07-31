def find_mid_ot_bench():
    lng, num = map(lambda i: int(i), input().split())
    l = list(map(lambda i: int(i), input().split()))

    ans_1 = 0
    ans_2 = 0

    for i in l:
        if lng % 2 == 1 and i == lng//2:
                print(i)
                return None
        elif i >= lng//2:
            ans_2 = i
            break

    j = l.index(ans_2)
    ans_1 = l[j-1]

    print(ans_1, ans_2)


find_mid_ot_bench()
