def check_folders():
    folders = int(input())
    diploms = list(map(lambda i: int(i), input().split()))

    result = 0
    m = 0
    for i in diploms:
        if i > m:
            m = i
        result += i

    print(result - m)


check_folders()