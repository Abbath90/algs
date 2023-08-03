def unique_elems(l):
    d = {}
    for i in l:
        if i in d:
            d[i] += 1
        else:
            d[i] = 0
    d = {key: val for key, val in d.items() if val == 0}
    print(" ".join(d.keys()))


l = input().split()

unique_elems(l)