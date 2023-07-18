INT_LIMIT = 2 * 10**9

students_number = int(input())
students_cords_string = input()
students_cords =  list(map(lambda x: int(x), students_cords_string.split(' ')))

def check_increasing_order(cords):
    for i, j in enumerate(cords):
        if i == len(cords) - 1:
            return True
        if not (j < cords[i+1]):
            return False

def validation_data(students_number, students_cords):
    if (
        (0 < students_number < 100001)
        and (len(students_cords) == students_number)
        and not any(i > INT_LIMIT for i in students_cords)
        and check_increasing_order(students_cords)
    ):
        return True
    raise AttributeError("Incorrect input data")


def count_spacing(students_number, students_cords):
    if validation_data(students_number, students_cords):
        return students_cords[students_number // 2]

print(count_spacing(students_number, students_cords))