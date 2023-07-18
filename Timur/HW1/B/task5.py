length = int(input())
point_cords_string = input()
point_cords =  list(map(lambda x: int(x), point_cords_string.split(' ')))


def validation_data(length, point_cords):
    if (
        (0 < length <= 1000)
        and (round(length) == length)
        and len(point_cords) == 2
        and all(-1000 <= i <= 1000 for i in point_cords)
    ):
        return True
    raise AttributeError("Incorrect input data")


def check_triangle(length, point_cords):
    if validation_data(length, point_cords):
        x, y = point_cords[0], point_cords[1]
        if x >= 0 and y >= 0 and x + y <= length:
            return 0
        return min(
            [
                (x**2 + y**2, 1),
                ((x - length)**2 + y**2, 2),
                (x**2 + (y - length)**2, 3),
            ]
        )[1]

print(check_triangle(length, point_cords))