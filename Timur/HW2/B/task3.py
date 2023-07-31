def repair_palindrome():
    s = list(input())
    lng = len(s)
    if lng % 2 == 1:
        left, right = s[:lng//2], s[(lng//2 + 1):]
    else:
        left, right = s[:lng//2], s[(lng//2):]

    counter = 0
    for i in range(len(left)):
        if left[i] != right[::-1][i]:
            counter += 1

    return counter


print(repair_palindrome())