def compare_lists(l1, l2):
    union_l = l1 + l2
    return len(union_l) - len(set(union_l))

l1 = list(map(lambda i: int(i), input().split()))
l2 = list(map(lambda i: int(i), input().split()))

print(compare_lists(l1, l2))