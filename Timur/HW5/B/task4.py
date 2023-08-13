OPEN = "("
CLOSE = ")"

def brackets(s):
    if s[0] == CLOSE:
        return "NO"
    cnt = 0
    for i in s:
        if i == OPEN:
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return "NO"

    if cnt == 0:
        return "YES"
    else:
        return "NO"

print(brackets(input()))
