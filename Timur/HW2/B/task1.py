def count_max():
    max_val = 0
    counter = 0
    while (val := int(input())) != 0:
        if val > max_val:
            max_val = val
            counter = 0
        if val == max_val:
            counter += 1
    return counter


print(count_max())