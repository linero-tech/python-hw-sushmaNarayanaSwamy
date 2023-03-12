from to_do import TODO


def task7(a, b):
    result = 1
    if a and b == 0:
        result = 1
    elif b == 1:
        result = a
    else:
        for power in range(b):
            result = result * a

    print(result)
    return result


if __name__ == "__main__":
    task7(2, 4)
    task7(6, 4)
    task7(4, 4)
    task7(3, 4)
    task7(10, 4)
    task7(20, 4)

