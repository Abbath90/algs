def check_value(l):
    d = dict.fromkeys(l, "NO")
    for i in l:
        ans = d[i]
        print(ans)
        if ans == "NO":
            d[i] = "YES"


l = list(map(lambda i: int(i), input().split()))

check_value(l)