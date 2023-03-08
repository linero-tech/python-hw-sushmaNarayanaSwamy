from to_do import TODO


def task1(a, b):
    if a >= b:
        result = 0
    else:
        result = 0
        for i in range(a, b+1):
            result += i

    return print(result)


if __name__ == "__main__":
    task1(1, 5)
    task1(3, 6)
    task1(3, 3)
