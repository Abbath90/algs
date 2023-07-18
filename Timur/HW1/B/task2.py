stantions, job, home = map(lambda x: int(x), input().split(' '))

def validation_data(stantions, job, home):
    if (
            (0 < stantions <= 100)
            and (0 < job <= stantions)
            and (0 < home <= stantions)
            and (job != home)
    ):
        return True
    raise AttributeError("Incorrect input data")


def stantion_checker(stantions, job, home):
    if validation_data(stantions, job, home):
        point1, point2 = min(job, home), max(job, home)
        return min([point2 - point1 - 1, abs(point2 - stantions) + point1 - 1])


print(stantion_checker(stantions, job, home))