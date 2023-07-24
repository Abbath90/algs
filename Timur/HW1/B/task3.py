val1, val2, val3 = map(lambda x: int(x), input().split(' '))


def validation_data(val1, val2, val3):
    if (
            (0 < val1 <= 31)
            and (0 < val2 <= 31)
            and (1970 <= val3 <= 2069)
            and ((val1 > 12 and val2 <= 12) or (val2 > 12 and val1 <= 12) or (val1 <= 12 and val2 <= 12))
    ):
        return True
    raise AttributeError("Incorrect input data")


def is_clear_date(val1, val2, val3):
    if validation_data(val1, val2, val3):
        if (
                ((val1 > 12) and (val2 <= 12))
                or (val2 > 12) and (val1 <= 12)
                or (val1 == val2)
        ):
            return "1"
        return "0"


print(is_clear_date(val1, val2, val3))
