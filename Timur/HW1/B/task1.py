code = int(input())
inter_score = int(input())
checker_score = int(input())


def validation_data(code, inter_score, checker_score):
    if (
            (-128 <= code <= 127)
            and (0 <= inter_score <= 7)
            and (0 <= checker_score <= 7)
    ):
        return True
    raise AttributeError("Incorrect input data")


def tester(code, inter_score, checker_score):
    result = inter_score
    if validation_data(code, inter_score, checker_score):
        if inter_score == 0:
            if code != 0:
                result = 3
            else:
                result = checker_score
        if inter_score == 1:
            result = checker_score
        if inter_score == 4:
            if code != 0:
                result = 3
            else:
                result = 4
        if inter_score == 6:
            result = 0
        if inter_score == 7:
            result = 1

    return result

print(tester(code, inter_score, checker_score))