SPACE = " "


n = int(input())
s = set(range(1, n + 1))
current_l = []
while (i:= input()) != "HELP":
    if SPACE in i:
        current_l = list(map(lambda j: int(j), i.split()))
    elif i.isdigit():
        current_l = [int(i)]
    if i == "YES":
        s.intersection_update(current_l)
    elif i == "NO":
        s.difference_update(current_l)

print(*sorted(s))